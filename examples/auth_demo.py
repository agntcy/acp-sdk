#!/usr/bin/env python
"""
Authorization Middleware Demo for AGNTCY ACP SDK

This example demonstrates how to use the authorization middleware 
to control access to agent actions based on user permissions.

It shows both:
1. Local authorization (policies defined in code)
2. Remote authorization via AuthZEN PDP (policies defined on a server)
"""

import os
import sys
import json
import logging
import uuid
import argparse
from typing import Dict, Any, Optional, Union

# Add the parent directory to the path to import the local agntcy_acp package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agntcy_acp import ACPClient
from agntcy_acp.auth import (
    # Local authorization components
    ACPAuthorization, 
    Permission,
    PermissionContext,
    PermissionDeniedError,
    
    # PDP (Policy Decision Point) components
    PDPClient,
    PDPAuthorization,
    
    # Shared components
    AuthorizationMiddleware,
    
    # Helper functions
    create_auth_service,
    create_pdp_auth_service
)

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Sample configuration
DEFAULT_CONFIG = {
    "host": "http://localhost:8080",
    "api_key": {"x-api-key": "demo-api-key"},
}

#####################################
# PART 1: LOCAL AUTHORIZATION DEMO  #
#####################################

# --- Define a custom policy checker ---
def is_admin_user(context: PermissionContext) -> bool:
    """Check if the user is an admin.
    
    This is a custom policy checker that can be added to the authorization service.
    """
    # In a real system, you would check the user's roles in a database
    admin_users = ["admin1", "admin2", "superuser"]
    return context.user_id in admin_users

# --- Define a role-based policy checker ---
def has_role_permission(context: PermissionContext) -> bool:
    """Check if the user's role has permission for this action.
    
    This demonstrates using the metadata field to pass role information.
    """
    # Get user roles from the metadata
    roles = context.metadata.get("roles", [])
    
    # Define role permissions
    role_permissions = {
        "viewer": ["get_stateless_run", "get_thread", "get_thread_run"],
        "agent_user": ["create_stateless_run", "create_thread", "create_thread_run"],
        "admin": ["*"]  # Wildcard for all actions
    }
    
    # Check if any of the user's roles grant permission for this action
    for role in roles:
        if role in role_permissions:
            allowed_actions = role_permissions[role]
            if "*" in allowed_actions or context.action in allowed_actions:
                return True
    
    return False

# --- Setup helper functions for local authorization ---
def setup_local_auth_service() -> ACPAuthorization:
    """Create and configure the local authorization service."""
    auth_service = ACPAuthorization()
    
    # Add custom policy checkers
    auth_service.add_policy_checker(is_admin_user)
    auth_service.add_policy_checker(has_role_permission)
    
    # Grant explicit permissions to users
    echo_agent_create_perm = Permission("echo-agent", "create_stateless_run")
    echo_agent_get_perm = Permission("echo-agent", "get_stateless_run")
    
    # Regular user can use echo-agent
    auth_service.grant_permission("user1", echo_agent_create_perm)
    auth_service.grant_permission("user1", echo_agent_get_perm)
    
    # Power user can use any agent for specific actions
    auth_service.grant_permission("power_user", Permission("*", "create_stateless_run"))
    auth_service.grant_permission("power_user", Permission("*", "get_stateless_run"))
    
    # Admin gets full access via the custom policy checker
    # (No explicit permissions needed)
    
    return auth_service


########################################
# PART 2: AUTHZEN PDP AUTHORIZATION    #
########################################

# --- Mock PDP Server for Demo ---
class MockPDPServer:
    """
    Mock Policy Decision Point server for demonstration.
    
    In a production environment, this would be replaced with a real AuthZEN-compatible server.
    """
    
    def __init__(self):
        self.permissions = {
            "user1": ["echo-agent:create_stateless_run", "echo-agent:get_stateless_run"],
            "power_user": ["*:create_stateless_run", "*:get_stateless_run"],
            "admin": ["*:*"],  # Admin can do anything
            "role_user": []  # Will be authorized via context roles
        }
        
    def evaluate_access(self, request_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process an access evaluation request."""
        subject = request_data.get("subject", {})
        subject_id = subject.get("id")
        
        resource = request_data.get("resource", {})
        resource_id = resource.get("id")
        
        action = request_data.get("action")
        context = request_data.get("context", {})
        
        # Default to deny
        decision = False
        
        # Simulate authorization logic
        if subject_id in self.permissions:
            allowed_actions = self.permissions[subject_id]
            
            # Check for exact match
            if f"{resource_id}:{action}" in allowed_actions:
                decision = True
            
            # Check for wildcard resource
            elif f"*:{action}" in allowed_actions:
                decision = True
                
            # Check for wildcard action
            elif f"{resource_id}:*" in allowed_actions:
                decision = True
                
            # Check for global wildcard
            elif "*:*" in allowed_actions:
                decision = True
                
            # Special case: role-based authorization
            # In a real PDP, this would be handled by the policy engine
            elif subject_id == "role_user" and context.get("roles"):
                roles = context.get("roles", [])
                if "agent_user" in roles and action in ["create_stateless_run", "create_thread", "create_thread_run"]:
                    decision = True
        
        # Simulate PDP response
        return {
            "decision": decision,
            "reason": "Demo PDP decision",
            "request_id": request_data.get("request_id", str(uuid.uuid4()))
        }

# Monkey patch the PDPClient for demo purposes
original_check_permission = PDPClient.check_permission

def mock_check_permission(self, *args, **kwargs):
    """Mock the check_permission method to use our mock PDP server."""
    try:
        # Convert kwargs to a request body
        request_data = {
            "subject": {
                "type": kwargs.get("subject_type", "user"),
                "id": kwargs.get("subject_id")
            },
            "action": kwargs.get("action"),
            "request_id": kwargs.get("request_id", str(uuid.uuid4()))
        }
        
        # Add resource if available
        if kwargs.get("resource_id") or kwargs.get("resource_type"):
            request_data["resource"] = {}
            if kwargs.get("resource_id"):
                request_data["resource"]["id"] = kwargs.get("resource_id")
            if kwargs.get("resource_type"):
                request_data["resource"]["type"] = kwargs.get("resource_type")
        
        # Add context if available
        if kwargs.get("context"):
            request_data["context"] = kwargs.get("context")
            
        # Call our mock PDP server
        mock_pdp = MockPDPServer()
        response = mock_pdp.evaluate_access(request_data)
        
        # Log the request and response for demonstration
        logger.info(f"PDP Request: {json.dumps(request_data)}")
        logger.info(f"PDP Response: {json.dumps(response)}")
        
        return response.get("decision", False)
    
    except Exception as e:
        logger.error(f"Error in mock PDP: {str(e)}")
        return False

# Apply the mock for demonstration
PDPClient.check_permission = mock_check_permission

# --- Setup helper function for PDP authorization ---
def setup_pdp_auth_service() -> PDPAuthorization:
    """Create and configure the PDP authorization service."""
    # In a real application, this would be your AuthZEN PDP server URL
    pdp_url = "https://pdp.example.com/api"
    
    # Optional token for PDP authentication
    pdp_token = "demo-token"
    
    # Create PDP client and auth service
    return create_pdp_auth_service(pdp_url, pdp_token)


########################################
# PART 3: SHARED CLIENT CREATION LOGIC #
########################################

def create_client(
    user_id: str, 
    auth_type: str = "local",
    roles: Optional[list] = None
) -> ACPClient:
    """Create an ACP client with authorization middleware.
    
    Args:
        user_id: The user ID to use for authorization
        auth_type: Type of authorization to use ('local' or 'pdp')
        roles: Optional list of roles to assign to the user
        
    Returns:
        Configured ACPClient with authorization middleware
    """
    # Create appropriate auth service based on type
    if auth_type == "pdp":
        auth_service = setup_pdp_auth_service()
    else:
        auth_service = setup_local_auth_service()
    
    # Create authorization middleware
    auth_middleware = AuthorizationMiddleware(auth_service)
    
    # Create the client with authorization
    client = ACPClient(
        configuration=DEFAULT_CONFIG,
        auth_middleware=auth_middleware
    )
    
    # Set the user context
    client.set_user_id(user_id)
    
    # Handle role-based auth for PDP 
    if auth_type == "pdp" and roles and user_id == "role_user":
        # For PDP, we need to patch the authorize method to include roles in context
        original_authorize = client.auth_middleware.authorize
        
        def authorize_with_roles(*args, **kwargs):
            # Add roles to the metadata/context
            kwargs["metadata"] = {"roles": roles}
            return original_authorize(*args, **kwargs)
        
        # Override the authorize method
        client.auth_middleware.authorize = authorize_with_roles
    
    return client


########################################
# PART 4: DEMO SCENARIOS               #
########################################

def demo_allowed_request(auth_type: str):
    """Demonstrate a request that should be allowed."""
    auth_name = "AuthZEN PDP" if auth_type == "pdp" else "Local"
    print(f"\n=== Allowed Request Demo ({auth_name}) ===")
    
    # Create a client for user1, who has permission for echo-agent
    client = create_client("user1", auth_type)
    
    try:
        # This should be allowed based on explicit permissions
        print(f"User1 attempting to create run with echo-agent...")
        response = client.create_stateless_run(
            agent_id="echo-agent",
            input={"messages": [{"type": "human", "content": "Hello, agent!"}]}
        )
        print(f"Success! Response: {response}")
    except PermissionDeniedError as e:
        print(f"Permission denied: {e}")
    except Exception as e:
        print(f"Error: {e}")

def demo_denied_request(auth_type: str):
    """Demonstrate a request that should be denied."""
    auth_name = "AuthZEN PDP" if auth_type == "pdp" else "Local"
    print(f"\n=== Denied Request Demo ({auth_name}) ===")
    
    # Create a client for user1, who doesn't have permission for gpt-agent
    client = create_client("user1", auth_type)
    
    try:
        # This should be denied - user1 only has permission for echo-agent
        print(f"User1 attempting to create run with gpt-agent...")
        response = client.create_stateless_run(
            agent_id="gpt-agent",
            input={"messages": [{"type": "human", "content": "Hello, agent!"}]}
        )
        print(f"Success! Response: {response}")
    except PermissionDeniedError as e:
        print(f"Permission denied: {e}")
    except Exception as e:
        print(f"Error: {e}")

def demo_role_based_authorization(auth_type: str):
    """Demonstrate role-based authorization using metadata."""
    auth_name = "AuthZEN PDP" if auth_type == "pdp" else "Local"
    print(f"\n=== Role-Based Authorization Demo ({auth_name}) ===")
    
    # Create a client for a user with the agent_user role
    client = create_client("role_user", auth_type, roles=["agent_user"])
    
    # For local auth, need to add roles to the authorization metadata
    if auth_type == "local":
        original_authorize = client.auth_middleware.authorize
        
        def authorize_with_roles(*args, **kwargs):
            # Add roles to the metadata
            kwargs["metadata"] = {"roles": ["agent_user"]}
            return original_authorize(*args, **kwargs)
        
        # Override the authorize method with our custom one
        client.auth_middleware.authorize = authorize_with_roles
    
    try:
        # This should be allowed based on the agent_user role
        print(f"Role user attempting to create run with any agent...")
        response = client.create_stateless_run(
            agent_id="any-agent",
            input={"messages": [{"type": "human", "content": "Hello, agent!"}]}
        )
        print(f"Success! Response: {response}")
    except PermissionDeniedError as e:
        print(f"Permission denied: {e}")
    except Exception as e:
        print(f"Error: {e}")

def demo_admin_user(auth_type: str):
    """Demonstrate admin user permissions via custom policy."""
    auth_name = "AuthZEN PDP" if auth_type == "pdp" else "Local"
    print(f"\n=== Admin User Demo ({auth_name}) ===")
    
    # Create a client for an admin user
    client = create_client("admin1", auth_type)
    
    try:
        # This should be allowed for the admin via policy
        print(f"Admin attempting to create run with restricted-agent...")
        response = client.create_stateless_run(
            agent_id="restricted-agent",
            input={"messages": [{"type": "human", "content": "Hello, agent!"}]}
        )
        print(f"Success! Response: {response}")
    except PermissionDeniedError as e:
        print(f"Permission denied: {e}")
    except Exception as e:
        print(f"Error: {e}")

def run_demo(auth_type: str):
    """Run all demos for the specified authorization type."""
    auth_name = "AuthZEN PDP" if auth_type == "pdp" else "Local"
    print(f"\n=== Running {auth_name} Authorization Demos ===")
    
    demo_allowed_request(auth_type)
    demo_denied_request(auth_type)
    demo_role_based_authorization(auth_type)
    demo_admin_user(auth_type)


########################################
# MAIN EXECUTION                       #
########################################

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="AGNTCY Authorization Demo")
    parser.add_argument(
        "--auth",
        choices=["local", "pdp", "both"],
        default="both",
        help="Authorization type to demo: local, pdp, or both"
    )
    args = parser.parse_args()
    
    # Mock the ACP client response method to avoid making actual API calls
    def mock_create_stateless_run(self, **kwargs):
        agent_id = kwargs.get("agent_id", "unknown")
        return {
            "id": "run_12345",
            "agent_id": agent_id,
            "status": "completed",
            "output": {
                "messages": [
                    {"type": "agent", "content": f"Hello from {agent_id}!"}
                ]
            }
        }
    
    # Apply the mock to the ACPClient class for demo purposes
    ACPClient.create_stateless_run = mock_create_stateless_run
    
    # Print header
    print("=== AGNTCY Authorization Demo ===")
    print("This demo shows different authorization approaches for AGNTCY ACP SDK.")
    print("")
    
    # Run the demos based on command line argument
    if args.auth == "local" or args.auth == "both":
        print("\n=== LOCAL AUTHORIZATION ===")
        print("Policies defined directly in code")
        run_demo("local")
        
    if args.auth == "pdp" or args.auth == "both":
        print("\n=== AUTHZEN PDP AUTHORIZATION ===")
        print("Policies defined on an external server following OpenID AuthZEN spec")
        run_demo("pdp")
        
    # Show how to choose between local and PDP in production
    print("\n=== HOW TO CHOOSE AUTHORIZATION TYPE ===")
    print("# Local authorization (policies in code)")
    print("auth_service = create_auth_service()")
    print("auth_middleware = AuthorizationMiddleware(auth_service)")
    print("")
    print("# AuthZEN PDP authorization (policies on server)")
    print("pdp_url = 'https://your-pdp-server.example.com/api'")
    print("pdp_auth = create_pdp_auth_service(pdp_url, token='your-auth-token')")
    print("auth_middleware = AuthorizationMiddleware(pdp_auth)")
    print("")
    print("# Create client with chosen middleware")
    print("client = ACPClient(auth_middleware=auth_middleware)")
    print("client.set_user_id('user123')")