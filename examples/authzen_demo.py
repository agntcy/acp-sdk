#!/usr/bin/env python
"""
AuthZEN PDP Authorization Demo for AGNTCY ACP SDK

This example demonstrates how to use the AuthZEN PDP integration for authorization.
It connects to an external Policy Decision Point (PDP) server to make authorization decisions.
"""

import os
import sys
import json
import logging
from typing import Dict, Any
import uuid

# Add the parent directory to the path to import the local agntcy_acp package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agntcy_acp import ACPClient
from agntcy_acp.auth import (
    create_pdp_client,
    create_pdp_auth_service,
    AuthorizationMiddleware,
    PDPClient,
    PDPAuthorization,
    PermissionDeniedError
)

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Sample configuration for ACP client
DEFAULT_CONFIG = {
    "host": "http://localhost:8080",
    "api_key": {"x-api-key": "demo-api-key"},
}

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
            "admin": ["*:*"]  # Admin can do anything
        }
        
    def evaluate_access(self, request_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process an access evaluation request."""
        subject = request_data.get("subject", {})
        subject_id = subject.get("id")
        
        resource = request_data.get("resource", {})
        resource_id = resource.get("id")
        
        action = request_data.get("action")
        
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

# --- Setup helper functions ---
def create_client(user_id: str) -> ACPClient:
    """Create an ACP client with PDP authorization middleware.
    
    Args:
        user_id: The user ID to use for authorization
        
    Returns:
        Configured ACPClient with PDP authorization
    """
    # In a real application, this would be your AuthZEN PDP server URL
    pdp_url = "https://pdp.example.com/api"
    
    # Optional token for PDP authentication
    pdp_token = "demo-token"
    
    # Create PDP client and auth service
    pdp_auth_service = create_pdp_auth_service(pdp_url, pdp_token)
    auth_middleware = AuthorizationMiddleware(pdp_auth_service)
    
    # Create the client with authorization
    client = ACPClient(
        configuration=DEFAULT_CONFIG,
        auth_middleware=auth_middleware
    )
    
    # Set the user context
    client.set_user_id(user_id)
    
    return client

# --- Demo scenarios ---
def demo_allowed_request():
    """Demonstrate a request that should be allowed."""
    print("\n=== Allowed Request Demo ===")
    
    # Create a client for user1, who has permission for echo-agent
    client = create_client("user1")
    
    try:
        # This should be allowed based on PDP response
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

def demo_denied_request():
    """Demonstrate a request that should be denied."""
    print("\n=== Denied Request Demo ===")
    
    # Create a client for user1, who doesn't have permission for gpt-agent
    client = create_client("user1")
    
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

def demo_power_user():
    """Demonstrate a power user with broader permissions."""
    print("\n=== Power User Demo ===")
    
    # Create a client for power_user, who has wildcard permissions
    client = create_client("power_user")
    
    try:
        # This should be allowed - power_user has wildcard agent permission
        print(f"Power user attempting to create run with any-agent...")
        response = client.create_stateless_run(
            agent_id="any-agent",
            input={"messages": [{"type": "human", "content": "Hello, agent!"}]}
        )
        print(f"Success! Response: {response}")
    except PermissionDeniedError as e:
        print(f"Permission denied: {e}")
    except Exception as e:
        print(f"Error: {e}")

def demo_admin_user():
    """Demonstrate admin user with full access."""
    print("\n=== Admin User Demo ===")
    
    # Create a client for admin who has full access
    client = create_client("admin")
    
    try:
        # This should be allowed - admin has full access
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

def run_all_demos():
    """Run all demonstration scenarios."""
    demo_allowed_request()
    demo_denied_request()
    demo_power_user()
    demo_admin_user()

# --- Real-world usage example ---
def production_example():
    """Example of how to use PDP authorization in a production environment."""
    print("\n=== Production Usage Example ===")
    print("# Configure PDP client with your AuthZEN PDP server")
    print("pdp_url = 'https://your-pdp-server.example.com/api'")
    print("pdp_token = 'your-authentication-token'")
    print("")
    print("# Create PDP auth service")
    print("pdp_auth_service = create_pdp_auth_service(pdp_url, pdp_token)")
    print("")
    print("# Create authorization middleware")
    print("auth_middleware = AuthorizationMiddleware(pdp_auth_service)")
    print("")
    print("# Create ACP client with middleware")
    print("client = ACPClient(")
    print("    configuration=your_acp_config,")
    print("    auth_middleware=auth_middleware")
    print(")")
    print("")
    print("# Set user ID for authorization")
    print("client.set_user_id('user-123')")
    print("")
    print("# Make API calls - authorization will be checked automatically")
    print("response = client.create_stateless_run(")
    print("    agent_id='echo-agent',")
    print("    input={'messages': [{'type': 'human', 'content': 'Hello'}]}")
    print(")")

# --- Main execution ---
if __name__ == "__main__":
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
    
    # Run the demos
    print("=== AuthZEN PDP Authorization Demo ===")
    print("This demo shows how to use an external Policy Decision Point (PDP)")
    print("for authorization decisions following the OpenID AuthZEN specification.")
    print("")
    run_all_demos()
    
    # Show production example
    production_example() 