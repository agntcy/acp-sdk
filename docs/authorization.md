# Authorization with ACP SDK

This document explains how to use the authorization feature in the ACP SDK, which implements the [AuthZEN API specification](https://openid.net/specs/authorization-api-1_0-01.html).

## Overview

The ACP SDK now supports optional authorization via a Policy Decision Point (PDP) that implements the AuthZEN API specification. This enables fine-grained access control for ACP requests based on subjects, resources, actions, and context.

## Configuration

To enable authorization, you need to configure the ACP client with a PDP URL and optionally an API key:

```python
from agntcy_acp.acp_v0 import Configuration
from agntcy_acp.authorization import configure_authorization

# Create configuration
config = Configuration()

# Configure authorization
configure_authorization(
    config,
    pdp_url="https://pdp.example.com",
    pdp_api_key="your-api-key",
    enable=True  # Default is True
)
```

## Authorization Process

When authorization is enabled, the ACP SDK will:

1. Before making any API request, send an authorization request to the configured PDP
2. Include the subject, resource, action, and context in the authorization request
3. Only proceed with the original API request if the PDP returns a positive decision
4. Raise an `UnauthorizedException` if access is denied

## Request Parameters

The AuthZEN API requires four main components in an authorization request:

### Subject

Represents the user or service making the request. You can create a subject using the helper function:

```python
from agntcy_acp.authorization import create_subject

subject = create_subject(
    subject_type="user",
    subject_id="alice@example.com",
    properties={
        "department": "Engineering",
        "role": "Developer"
    }
)
```

### Resource

Represents the target of the request. Create a resource using:

```python
from agntcy_acp.authorization import create_resource

resource = create_resource(
    resource_type="agent",
    resource_id="agent-123",
    properties={
        "owner": "bob@example.com",
        "classification": "internal"
    }
)
```

### Action

Represents the operation being performed. Create an action using:

```python
from agntcy_acp.authorization import create_action

action = create_action(
    action_type="read"  # Or "write", "delete", etc.
)
```

### Context

Additional contextual information about the request, provided as a dictionary:

```python
context = {
    "ip_address": "192.168.1.100",
    "device_id": "laptop-xyz",
    "timestamp": "2023-06-15T14:30:00Z"
}
```

## Using with API Clients

### Synchronous Client

```python
from agntcy_acp.acp_v0.sync_client.api_client import ApiClient

api_client = ApiClient(configuration=config)

try:
    response = api_client.call_api(
        method="GET",
        url="/agents/agent-123",
        subject=subject,
        resource=resource,
        action=action,
        context=context
    )
    # Process response
except UnauthorizedException:
    # Handle authorization failure
```

### Asynchronous Client

```python
from agntcy_acp.acp_v0.async_client.api_client import ApiClient as AsyncApiClient

async with AsyncApiClient(configuration=config) as api_client:
    try:
        response = await api_client.call_api(
            method="GET",
            url="/agents/agent-123",
            subject=subject,
            resource=resource,
            action=action,
            context=context
        )
        # Process response
    except UnauthorizedException:
        # Handle authorization failure
```

## Default Values

If you don't provide explicit values for subject, resource, action, or context, the SDK will generate reasonable defaults:

- **Subject**: Uses the configured username or "anonymous" as the subject ID
- **Resource**: Derives the resource type and ID from the request URL
- **Action**: Uses the HTTP method (e.g., "get", "post") as the action type
- **Context**: Empty by default

## Example Implementation

See the `examples/authorization_example.py` and `examples/async_authorization_example.py` files for complete working examples. 