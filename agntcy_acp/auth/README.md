# Authorization Middleware for AGNTCY ACP SDK

This module provides authorization capabilities for the AGNTCY ACP SDK, allowing you to control access to agent actions based on user permissions.

## Features

- **Permission-based authorization**: Define and check permissions for agent actions
- **Role-based access control**: Assign permissions to roles, and roles to users
- **Custom policy support**: Add your own authorization logic through policy checkers
- **Contextual authorization**: Use metadata for dynamic authorization decisions
- **Flexible permission model**: Support for wildcards, resource-specific permissions, and more
- **AuthZEN PDP integration**: Connect to an external Policy Decision Point (PDP) for authorization decisions

## Basic Usage

### Local Authorization

Here's a simple example of using local authorization:

```python
from agntcy_acp import ACPClient
from agntcy_acp.auth import (
    ACPAuthorization, 
    AuthorizationMiddleware, 
    Permission
)

# Create and configure the authorization service
auth_service = ACPAuthorization()

# Grant a permission to a user
permission = Permission(agent_id="echo-agent", action="create_stateless_run")
auth_service.grant_permission(user_id="user123", permission=permission)

# Create the middleware
auth_middleware = AuthorizationMiddleware(auth_service)

# Create the ACP client with middleware
client = ACPClient(
    configuration={"host": "http://localhost:8080", "api_key": {"x-api-key": "demo-key"}},
    auth_middleware=auth_middleware
)

# Set the user context
client.set_user_id("user123")

# Make a request (this will be checked against permissions)
response = client.create_stateless_run(
    agent_id="echo-agent",
    input={"messages": [{"type": "human", "content": "Hello!"}]}
)
```

### AuthZEN PDP Integration

Connect to an external Policy Decision Point (PDP) for authorization decisions:

```python
from agntcy_acp import ACPClient
from agntcy_acp.auth import (
    create_pdp_auth_service,
    AuthorizationMiddleware
)

# Create a PDP-based authorization service
pdp_url = "https://your-pdp-server.example.com/api"
pdp_token = "your-auth-token"  # Optional
pdp_auth_service = create_pdp_auth_service(pdp_url, pdp_token)

# Create authorization middleware
auth_middleware = AuthorizationMiddleware(pdp_auth_service)

# Create ACP client with middleware
client = ACPClient(
    configuration={"host": "http://localhost:8080", "api_key": {"x-api-key": "demo-key"}},
    auth_middleware=auth_middleware
)

# Set the user context
client.set_user_id("user123")

# Make requests - authorization will be checked via the PDP
response = client.create_stateless_run(
    agent_id="echo-agent",
    input={"messages": [{"type": "human", "content": "Hello!"}]}
)
```

## Permission Models

### Local Permission Model

The local authorization system uses a hierarchical permission model:

1. **Explicit permissions**: Permissions granted directly to a user
2. **Wildcard permissions**: Permissions that apply to all agents or all actions
3. **Custom policies**: Programmatic rules that can check any aspect of the request

Permissions are defined with:

- `agent_id`: The agent the permission applies to (or `"*"` for all agents)
- `action`: The action being performed (or `"*"` for all actions)
- `resource_id`: Optional specific resource (like a thread ID) the permission applies to

### AuthZEN PDP Model

When using the PDP integration, authorization decisions are delegated to an external service following the OpenID AuthZEN protocol:

- **Subject**: The user making the request
- **Action**: The operation being performed
- **Resource**: The agent or resource being accessed
- **Context**: Additional information about the request

The PDP receives these details and returns a yes/no decision that is enforced by the middleware.

## Advanced Usage

### Custom Policy Checkers (Local Authorization)

You can add custom logic for authorization decisions:

```python
def is_admin_user(context):
    """Check if the user is an admin."""
    admin_users = ["admin1", "admin2"]
    return context.user_id in admin_users

# Add the policy checker to the auth service
auth_service.add_policy_checker(is_admin_user)
```

### Role-Based Access Control (Local Authorization)

Implement RBAC by passing role information in the metadata:

```python
# Define role permissions in a custom policy checker
def has_role_permission(context):
    roles = context.metadata.get("roles", [])
    # Define permissions for each role
    role_permissions = {
        "viewer": ["get_stateless_run"],
        "user": ["create_stateless_run", "get_stateless_run"],
        "admin": ["*"]  # All permissions
    }
    
    for role in roles:
        if role in role_permissions:
            allowed_actions = role_permissions[role]
            if "*" in allowed_actions or context.action in allowed_actions:
                return True
    return False

# Add the role checker
auth_service.add_policy_checker(has_role_permission)

# When making a request, include role information
client._authorize(
    agent_id="echo-agent", 
    action="create_stateless_run",
    metadata={"roles": ["user"]}
)
```

### Custom PDP Headers and Configuration

For advanced PDP configuration:

```python
from agntcy_acp.auth import PDPClient, PDPAuthorization, AuthorizationMiddleware

# Create a PDP client with custom headers and configuration
pdp_client = PDPClient(
    pdp_url="https://pdp.example.com/api",
    token="oauth-token",
    headers={"X-Custom-Header": "value"},
    timeout=10
)

# Create authorization service and middleware
pdp_auth = PDPAuthorization(pdp_client)
auth_middleware = AuthorizationMiddleware(pdp_auth)

# Use the middleware with an ACP client
client = ACPClient(auth_middleware=auth_middleware)
```

### Integration with Agent Manifests

You can extend the Agent Manifest schema to include permission requirements:

```yaml
name: echo-agent
# ... other manifest fields ...
specs:
  # ... other specs ...
  permissions:
    - name: use_agent
      description: Basic permission to use this agent
      actions:
        - create_stateless_run
        - get_stateless_run
```

## API Reference

### Local Authorization Components

#### `Permission`

Represents a permission for an agent action.

```python
Permission(agent_id="echo-agent", action="create_stateless_run", resource_id=None)
```

#### `ACPAuthorization`

Manages permissions and policies.

```python
# Create the service
auth_service = ACPAuthorization()

# Grant a permission
auth_service.grant_permission(user_id, permission)

# Revoke a permission
auth_service.revoke_permission(user_id, permission)

# Add a policy checker
auth_service.add_policy_checker(checker_function)

# Check a permission directly
has_permission = auth_service.check_permission(context)
```

### AuthZEN PDP Components

#### `PDPClient`

Client for connecting to an AuthZEN-compatible Policy Decision Point.

```python
# Create a PDP client
pdp_client = PDPClient(
    pdp_url="https://pdp.example.com/api",
    token="auth-token",  # Optional
    headers={"Custom-Header": "value"},  # Optional
    timeout=5  # Optional, in seconds
)

# Check a permission directly
allowed = pdp_client.check_permission(
    subject_id="user123",
    subject_type="user",  # Optional, defaults to "user"
    subject_properties={"department": "sales"},  # Optional
    resource_id="echo-agent",
    resource_type="agent",  # Optional
    action="create_stateless_run",
    context={"ip_address": "192.168.1.1"},  # Optional
    request_id="req-123"  # Optional
)
```

#### `PDPAuthorization`

Adapter that makes PDPClient compatible with the authorization middleware.

```python
# Create a PDP authorization service
pdp_auth = PDPAuthorization(pdp_client)

# Check a permission
allowed = pdp_auth.check_permission(
    user_id="user123",
    agent_id="echo-agent",
    action="create_stateless_run",
    resource_id=None,  # Optional
    metadata={"ip_address": "192.168.1.1"}  # Optional
)
```

### Middleware

#### `AuthorizationMiddleware`

Middleware that integrates with the ACPClient. Works with both local and PDP-based authorization.

```python
# Create middleware
middleware = AuthorizationMiddleware(auth_service)  # Can be ACPAuthorization or PDPAuthorization

# Check permission (returns True/False)
allowed = middleware.check_permission(
    user_id="user123",
    agent_id="echo-agent",
    action="create_stateless_run"
)

# Authorize (raises PermissionDeniedError if not allowed)
middleware.authorize(
    user_id="user123",
    agent_id="echo-agent",
    action="create_stateless_run",
    resource_id=None,
    metadata={"roles": ["user"]}
)
```

### Helper Functions

```python
# Create a local authorization service
auth_service = create_auth_service()

# Create authorization middleware
middleware = create_middleware(auth_service)

# Create a PDP client
pdp_client = create_pdp_client(pdp_url="https://pdp.example.com", token="auth-token")

# Create a PDP authorization service
pdp_auth = create_pdp_auth_service(pdp_url="https://pdp.example.com", token="auth-token")
```

## Error Handling

```python
from agntcy_acp.auth import PermissionDeniedError

try:
    response = client.create_stateless_run(agent_id="restricted-agent", input=input_data)
except PermissionDeniedError as e:
    print(f"Permission denied: {e}")
    # Handle the permission denial
except Exception as e:
    print(f"Other error: {e}")
```

## Demos

For complete examples, see:
- `examples/auth_demo.py` - Local authorization demo
- `examples/authzen_demo.py` - AuthZEN PDP integration demo 