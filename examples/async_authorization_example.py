#!/usr/bin/env python
# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0

"""
Example script demonstrating how to use authorization with the ACP SDK's async client.

This example shows how to:
1. Configure the async client with authorization settings
2. Create and use authorization parameters
3. Handle authorization failures asynchronously
"""

import sys
import os
import asyncio
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agntcy_acp.acp_v0 import Configuration
from agntcy_acp.acp_v0.async_client.api_client import ApiClient as AsyncApiClient
from agntcy_acp.authorization import (
    configure_authorization,
    create_subject,
    create_resource,
    create_action
)
from agntcy_acp.acp_v0.exceptions import UnauthorizedException

async def main():
    # Create and configure client
    config = Configuration()
    
    # Enable authorization with PDP URL and API key
    configure_authorization(
        config,
        pdp_url="https://pdp.example.com",
        pdp_api_key="your-api-key-here"
    )
    
    # Create async API client
    async with AsyncApiClient(configuration=config) as api_client:
        # Example subject, resource, action, and context
        subject = create_subject(
            subject_type="user",
            subject_id="alice@example.com",
            properties={
                "department": "Engineering",
                "role": "Senior Developer"
            }
        )
        
        resource = create_resource(
            resource_type="agent",
            resource_id="agent-123",
            properties={
                "owner": "bob@example.com",
                "sensitivity": "low"
            }
        )
        
        action = create_action(
            action_type="read"
        )
        
        context = {
            "ip_address": "192.168.1.100",
            "device_id": "laptop-xyz",
            "timestamp": "2023-06-15T14:30:00Z"
        }
        
        try:
            # Make an async API call with authorization parameters
            response = await api_client.call_api(
                method="GET",
                url="/agents/agent-123",
                subject=subject,
                resource=resource,
                action=action,
                context=context
            )
            
            print("Request authorized and completed successfully!")
            
        except UnauthorizedException as e:
            print(f"Authorization failed: {e}")
            # Handle the authorization failure
            
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main()) 