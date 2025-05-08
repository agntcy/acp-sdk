# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
from .acp_v0.sync_client.api_client import ApiClient
from .acp_v0.async_client.api_client import ApiClient as AsyncApiClient
from .acp_v0 import ApiResponse
from .acp_v0.spec_version import VERSION as ACP_VERSION
from .acp_v0.spec_version import MAJOR_VERSION as ACP_MAJOR_VERSION
from .acp_v0.spec_version import MINOR_VERSION as ACP_MINOR_VERSION
from .agws_v0.spec_version import VERSION as AGWS_VERSION
from .agws_v0.spec_version import MAJOR_VERSION as AGWS_MAJOR_VERSION
from .agws_v0.spec_version import MINOR_VERSION as AGWS_MINOR_VERSION
from .exceptions import ACPDescriptorValidationException, ACPRunException
from .client import ApiClientConfiguration, ACPClient, AsyncACPClient
from agntcy_acp.acp_v0.exceptions import (
    OpenApiException, 
    ApiTypeError,
    ApiValueError,
    ApiKeyError,
    ApiAttributeError,
    ApiException,
    BadRequestException,
    NotFoundException,
    UnauthorizedException,
    ForbiddenException,
    ServiceException,
    ConflictException,
    UnprocessableEntityException,
)

# Try to import authorization components if available
try:
    from .auth import (
        ACPAuthorization,
        AuthorizationMiddleware,
        Permission,
        PermissionContext,
        PermissionDeniedError,
    )
except ImportError:
    pass

__all__ = [
    "ACPClient",
    "ApiClient",
    "AsyncACPClient",
    "AsyncApiClient",
    "ApiClientConfiguration",
    "ApiResponse",
    "ACPDescriptorValidationException",
    "ACPRunException",
    "OpenApiException", 
    "ApiTypeError",
    "ApiValueError",
    "ApiKeyError",
    "ApiAttributeError",
    "ApiException",
    "BadRequestException",
    "NotFoundException",
    "UnauthorizedException",
    "ForbiddenException",
    "ServiceException",
    "ConflictException",
    "UnprocessableEntityException",
    "ACP_VERSION",
    "ACP_MAJOR_VERSION",
    "ACP_MINOR_VERSION",
    "AGWS_VERSION",
    "AGWS_MINOR_VERSION",
    "AGWS_MAJOR_VERSION",
]
