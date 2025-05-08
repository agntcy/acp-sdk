"""
PDP (Policy Decision Point) client for AuthZEN authorization.

Implements the OpenID AuthZEN Authorization API 1.0 protocol.
https://openid.net/specs/authorization-api-1_0-01.html
"""
import json
import logging
from typing import Dict, Any, Optional, List, Union
import requests
from urllib.parse import urljoin

logger = logging.getLogger(__name__)

class PDPClient:
    """Client for communicating with an AuthZEN-compatible Policy Decision Point."""
    
    def __init__(
        self, 
        pdp_url: str,
        token: Optional[str] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: int = 5
    ):
        """Initialize a PDP client.
        
        Args:
            pdp_url: URL of the Policy Decision Point
            token: Optional authentication token
            headers: Additional headers to include in requests
            timeout: Request timeout in seconds
        """
        self.pdp_url = pdp_url.rstrip("/")
        self.token = token
        self.headers = headers or {}
        self.timeout = timeout
        
        # Add token to headers if provided
        if token:
            self.headers["Authorization"] = f"Bearer {token}"
        
        # Set content type for AuthZEN API
        self.headers["Content-Type"] = "application/json"
    
    def check_permission(
        self,
        subject_id: str,
        subject_type: str = "user",
        subject_properties: Optional[Dict[str, Any]] = None,
        resource_id: Optional[str] = None,
        resource_type: Optional[str] = None,
        action: str = "use",
        context: Optional[Dict[str, Any]] = None,
        request_id: Optional[str] = None
    ) -> bool:
        """Check if a subject has permission to perform an action on a resource.
        
        Args:
            subject_id: ID of the subject (user)
            subject_type: Type of subject (default: "user")
            subject_properties: Additional properties of the subject
            resource_id: ID of the resource
            resource_type: Type of resource
            action: The action being performed
            context: Additional context for the decision
            request_id: Optional request ID for tracking
            
        Returns:
            True if permission is granted, False otherwise
        """
        url = urljoin(self.pdp_url, "/v1/evaluate/access")
        
        # Prepare request headers
        headers = self.headers.copy()
        if request_id:
            headers["X-Request-ID"] = request_id
        
        # Build the request body according to AuthZEN spec
        body = {
            "subject": {
                "type": subject_type,
                "id": subject_id
            },
            "action": action
        }
        
        # Add subject properties if available
        if subject_properties:
            body["subject"]["properties"] = subject_properties
            
        # Add resource if available
        if resource_id or resource_type:
            body["resource"] = {}
            if resource_id:
                body["resource"]["id"] = resource_id
            if resource_type:
                body["resource"]["type"] = resource_type
                
        # Add context if available
        if context:
            body["context"] = context
            
        try:
            response = requests.post(
                url,
                headers=headers,
                json=body,
                timeout=self.timeout
            )
            
            # Check for HTTP errors
            response.raise_for_status()
            
            # Parse response
            result = response.json()
            
            # According to AuthZEN spec, the decision is in the "decision" field
            # True means "allow", False means "deny"
            return result.get("decision", False)
            
        except requests.RequestException as e:
            logger.error(f"Error calling PDP: {str(e)}")
            # Default to deny on error
            return False


class PDPAuthorization:
    """Authorization service that delegates decisions to a PDP."""
    
    def __init__(self, pdp_client: PDPClient):
        """Initialize authorization with a PDP client.
        
        Args:
            pdp_client: The PDP client to use for authorization decisions
        """
        self.pdp_client = pdp_client
        
    def check_permission(self, 
                       user_id: str, 
                       agent_id: str, 
                       action: str, 
                       resource_id: Optional[str] = None,
                       metadata: Optional[Dict[str, Any]] = None) -> bool:
        """Check if a user has permission to perform an action on an agent.
        
        Args:
            user_id: ID of the user
            agent_id: ID of the agent
            action: The action being performed
            resource_id: Optional ID of a specific resource
            metadata: Additional context for the decision
            
        Returns:
            True if permission is granted, False otherwise
        """
        # Convert ACP authorization model to AuthZEN model
        context = metadata or {}
        
        # Add additional context about the agent if not used as a resource
        if agent_id and agent_id != "*":
            context["agent_id"] = agent_id
            
        # Determine resource
        resource_id_to_use = resource_id
        resource_type = None
        
        # If we have a specific agent, use it as the resource
        if agent_id and agent_id != "*":
            resource_id_to_use = agent_id
            resource_type = "agent"
            
        return self.pdp_client.check_permission(
            subject_id=user_id,
            subject_type="user",
            resource_id=resource_id_to_use,
            resource_type=resource_type,
            action=action,
            context=context
        ) 