# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
# coding: utf-8

"""
Authorization utilities for the Agent Connect Protocol.

This module provides helper functions for configuring and using
the AuthZEN authorization with the ACP SDK.
"""

from typing import Dict, Any, Optional, Union

def create_subject(subject_type: str, subject_id: str, properties: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Create a subject object for authorization requests.
    
    :param subject_type: The type of the subject (e.g., "user", "service")
    :param subject_id: The unique identifier of the subject
    :param properties: Optional additional properties for the subject
    :return: A subject object compatible with AuthZEN API
    """
    subject = {
        "type": subject_type,
        "id": subject_id
    }
    
    if properties:
        subject["properties"] = properties
        
    return subject

def create_resource(resource_type: str, resource_id: str, properties: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Create a resource object for authorization requests.
    
    :param resource_type: The type of the resource (e.g., "document", "endpoint")
    :param resource_id: The unique identifier of the resource
    :param properties: Optional additional properties for the resource
    :return: A resource object compatible with AuthZEN API
    """
    resource = {
        "type": resource_type,
        "id": resource_id
    }
    
    if properties:
        resource["properties"] = properties
        
    return resource

def create_action(action_type: str, properties: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Create an action object for authorization requests.
    
    :param action_type: The type of action (e.g., "read", "write", "delete", or HTTP methods)
    :param properties: Optional additional properties for the action
    :return: An action object compatible with AuthZEN API
    """
    action = {
        "type": action_type
    }
    
    if properties:
        action["properties"] = properties
        
    return action

def configure_authorization(config, pdp_url: str, pdp_api_key: Optional[str] = None, enable: bool = True) -> None:
    """
    Configure authorization settings for an ACP client configuration.
    
    :param config: ACP client configuration object
    :param pdp_url: URL for the Policy Decision Point (PDP) server
    :param pdp_api_key: Optional API key for the PDP server
    :param enable: Whether to enable authorization (default: True)
    """
    config.pdp_url = pdp_url
    config.pdp_api_key = pdp_api_key
    config.authz_enabled = enable

# Example usage:
"""
from agntcy_acp.acp_v0 import Configuration
from agntcy_acp.acp_v0.sync_client.api_client import ApiClient
from agntcy_acp.authorization import configure_authorization, create_subject, create_resource, create_action

# Create configuration
config = Configuration()

# Configure authorization
configure_authorization(
    config,
    pdp_url="https://pdp.example.com",
    pdp_api_key="your-api-key"
)

# Create API client
api_client = ApiClient(configuration=config)

# Make a request with authorization parameters
response = api_client.call_api(
    method="GET",
    url="/agents/agent123",
    subject=create_subject("user", "alice@example.com", {"department": "Engineering"}),
    resource=create_resource("agent", "agent123"),
    action=create_action("read"),
    context={"ip_address": "192.168.1.100"}
)

# Or with async client:
# async_client = AsyncApiClient(configuration=config)
# response = await async_client.call_api(...)
""" 