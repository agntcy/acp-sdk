"""
Authorization module for AGNTCY ACP SDK.

Provides middleware and utilities for authorizing agent actions.
"""
from typing import Dict, List, Set, Callable, Optional, Any, Union

# Import PDP client if available
try:
    from .pdp_client import PDPClient, PDPAuthorization
except ImportError:
    # Stubs in case requests is not installed
    class PDPClient:
        def __init__(self, *args, **kwargs):
            raise ImportError("requests package is required for PDPClient")
    
    class PDPAuthorization:
        def __init__(self, *args, **kwargs):
            raise ImportError("requests package is required for PDPAuthorization")


class Permission:
    """Represents a permission for an agent action."""
    
    def __init__(self, agent_id: str, action: str, resource_id: Optional[str] = None):
        self.agent_id = agent_id
        self.action = action
        self.resource_id = resource_id
    
    def __str__(self) -> str:
        if self.resource_id:
            return f"agent:{self.agent_id}:resource:{self.resource_id}:{self.action}"
        return f"agent:{self.agent_id}:{self.action}"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Permission):
            return False
        return (self.agent_id == other.agent_id and 
                self.action == other.action and 
                self.resource_id == other.resource_id)
    
    def __hash__(self) -> int:
        return hash((self.agent_id, self.action, self.resource_id))


class PermissionContext:
    """Holds context for a permission check."""
    
    def __init__(self, 
                 user_id: str, 
                 agent_id: str, 
                 action: str, 
                 resource_id: Optional[str] = None,
                 metadata: Optional[Dict[str, Any]] = None):
        self.user_id = user_id
        self.agent_id = agent_id
        self.action = action
        self.resource_id = resource_id
        self.metadata = metadata or {}
    
    def __str__(self) -> str:
        if self.resource_id:
            return f"User '{self.user_id}' -> Agent '{self.agent_id}' -> Action '{self.action}' -> Resource '{self.resource_id}'"
        return f"User '{self.user_id}' -> Agent '{self.agent_id}' -> Action '{self.action}'"


class PermissionDeniedError(Exception):
    """Raised when a user does not have permission for an action."""
    
    def __init__(self, context: PermissionContext):
        self.context = context
        super().__init__(f"Permission denied: {str(context)}")


class ACPAuthorization:
    """Permission manager for ACP agents."""
    
    def __init__(self):
        # Map of user_id -> set of permissions
        self.user_permissions: Dict[str, Set[Permission]] = {}
        # Custom policy checkers with signature: (context: PermissionContext) -> bool
        self.policy_checkers: List[Callable[[PermissionContext], bool]] = []
    
    def grant_permission(self, user_id: str, permission: Permission) -> None:
        """Grant a permission to a user."""
        if user_id not in self.user_permissions:
            self.user_permissions[user_id] = set()
        self.user_permissions[user_id].add(permission)
    
    def revoke_permission(self, user_id: str, permission: Permission) -> None:
        """Revoke a permission from a user."""
        if user_id in self.user_permissions:
            self.user_permissions[user_id].discard(permission)
    
    def add_policy_checker(self, checker: Callable[[PermissionContext], bool]) -> None:
        """Add a custom policy checker function."""
        self.policy_checkers.append(checker)
    
    def check_permission(self, context: PermissionContext) -> bool:
        """Check if user has permission for the given context."""
        user_id = context.user_id
        agent_id = context.agent_id
        action = context.action
        resource_id = context.resource_id
        
        # If user doesn't exist, deny by default
        if user_id not in self.user_permissions:
            return False
        
        # Check specific permission
        permission = Permission(agent_id, action, resource_id)
        if permission in self.user_permissions[user_id]:
            return True
        
        # Check agent-level permission (without resource)
        agent_permission = Permission(agent_id, action)
        if agent_permission in self.user_permissions[user_id]:
            return True
        
        # Check wildcard agent permission
        wildcard_permission = Permission("*", action, resource_id)
        if wildcard_permission in self.user_permissions[user_id]:
            return True
        
        # Check wildcard action permission
        wildcard_action_permission = Permission(agent_id, "*", resource_id)
        if wildcard_action_permission in self.user_permissions[user_id]:
            return True
        
        # Check global wildcard permission
        global_wildcard = Permission("*", "*")
        if global_wildcard in self.user_permissions[user_id]:
            return True
        
        # Run through custom policy checkers
        for checker in self.policy_checkers:
            if checker(context):
                return True
        
        return False


class AuthorizationMiddleware:
    """Middleware for checking permissions on ACP requests."""
    
    def __init__(self, auth_service: Union[ACPAuthorization, PDPAuthorization]):
        """Initialize middleware with an authorization service.
        
        Args:
            auth_service: Authorization service to use for permission checks.
                         Can be either ACPAuthorization (local) or PDPAuthorization (remote).
        """
        self.auth_service = auth_service
    
    def check_permission(self, 
                        user_id: str, 
                        agent_id: str, 
                        action: str, 
                        resource_id: Optional[str] = None,
                        metadata: Optional[Dict[str, Any]] = None) -> bool:
        """Check if a user has permission to perform an action."""
        if isinstance(self.auth_service, ACPAuthorization):
            # Use local permission check for ACPAuthorization
            context = PermissionContext(
                user_id=user_id,
                agent_id=agent_id,
                action=action,
                resource_id=resource_id,
                metadata=metadata
            )
            return self.auth_service.check_permission(context)
        else:
            # Use direct check for PDPAuthorization
            return self.auth_service.check_permission(
                user_id=user_id,
                agent_id=agent_id,
                action=action,
                resource_id=resource_id,
                metadata=metadata
            )
    
    def authorize(self, 
                 user_id: str, 
                 agent_id: str, 
                 action: str, 
                 resource_id: Optional[str] = None,
                 metadata: Optional[Dict[str, Any]] = None) -> None:
        """Authorize an action, raising PermissionDeniedError if not permitted."""
        if not self.check_permission(
            user_id=user_id,
            agent_id=agent_id,
            action=action,
            resource_id=resource_id,
            metadata=metadata
        ):
            context = PermissionContext(
                user_id=user_id,
                agent_id=agent_id,
                action=action,
                resource_id=resource_id,
                metadata=metadata
            )
            raise PermissionDeniedError(context)


# Utility functions
def create_auth_service() -> ACPAuthorization:
    """Create and return a new authorization service."""
    return ACPAuthorization()


def create_middleware(auth_service: Union[ACPAuthorization, PDPAuthorization]) -> AuthorizationMiddleware:
    """Create and return middleware using the given auth service."""
    return AuthorizationMiddleware(auth_service)


def create_pdp_client(pdp_url: str, token: Optional[str] = None) -> PDPClient:
    """Create a PDP client for remote authorization.
    
    Args:
        pdp_url: URL of the Policy Decision Point server
        token: Optional authentication token
        
    Returns:
        Configured PDPClient instance
    """
    return PDPClient(pdp_url=pdp_url, token=token)


def create_pdp_auth_service(pdp_url: str, token: Optional[str] = None) -> PDPAuthorization:
    """Create a PDP-based authorization service.
    
    Args:
        pdp_url: URL of the Policy Decision Point server
        token: Optional authentication token
        
    Returns:
        Configured PDPAuthorization instance
    """
    pdp_client = create_pdp_client(pdp_url, token)
    return PDPAuthorization(pdp_client)


__all__ = [
    'ACPAuthorization',
    'AuthorizationMiddleware',
    'PDPClient',
    'PDPAuthorization',
    'Permission',
    'PermissionContext',
    'PermissionDeniedError',
    'create_auth_service',
    'create_middleware',
    'create_pdp_client',
    'create_pdp_auth_service',
] 