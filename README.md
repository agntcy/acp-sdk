# Agent Connect Protocol SDK

[![PyPI version](https://img.shields.io/pypi/v/agntcy-acp.svg)](https://pypi.org/project/agntcy-acp/)

## About The Project

The "Agent Connect Protocol SDK" is an open-source library designed to facilitate the adoption of the Agent Connect Protocol.
It offers tools for both client and server implementations, enabling seamless integration and communication between multi-agent systems.

## Getting Started

See [Getting Started Guide](https://agntcy.github.io/acp-sdk/README.md#getting-started)


## Documentation

See [ACP SDK Documentation](https://agntcy.github.io/acp-sdk) to deep dive.

See [IoA Documentation](https://docs.agntcy.org) for more info on Internet of Agents.

## Testing

`make test`


## Building the package

⚠️ Note: this step is only necessary for maintainers of the project. ⚠️

The [agntcy-acp Python package](https://pypi.org/project/agntcy-acp/) is
built on GitHub and published using GitHub actions. The action can be found
in the relevant workflows directory in the repo. The project attempts to keep
the SDK updated on any ACP or relevant specification changes, but delays can
happen.

### Prerequisites

This repo uses the following tools to build (or update) the packages:
  * jq: to parse OpenAPI JSON
  * poetry: to manage Python dependencies
  * make: to store command recipes
  * docker: to run the 
  [openapi-generator-cli](https://github.com/OpenAPITools/openapi-generator-cli) tool
  * git: to checkout the source specifications

### Generating the SDK clients from the OpenAPI ACP specification

There are two make targets to generate the clients:
  * `make generate_acp_client`
  * `make generate_acp_async_client`

Note that the make targets add a SPDX header and update the package 
imports to match the files as they should appear in the `agntcy_acp/acp_vXX`
subpackages. Please check the Makefile for questions on how this is done.

To update the `agntcy_acp` package by copying the relevant files, use: 
`make update_python_subpackage`

### Updating the client package on a new ACP specification release

For a minor release, follow these steps:

  1. Run: `ACP_SPEC_RELEASE=<RELEASE_TAG> make update_python_subpackage` 
  using the relevant "<RELEASE_TAG>"
  2. Check for any irregularities: `git diff`
  3. Run: `make test`

For a major release, follow these steps:

  1. Run: `ACP_SPEC_RELEASE=<RELEASE_TAG> make update_python_subpackage` 
  using the relevant "<RELEASE_TAG>"
  2. Update the version imports if you want to change the default major
  version in:
      * `agntcy_acp/__init__.py`
      * `agntcy_acp/models/__init__.py`
  3. Check for any irregularities: `git diff`
  4. Run: `make test`

### Publishing

Publishing the package uses a GitHub action triggered by 
assigning tags to commits of the form `v<PACKAGE_VERSION>`.

The tag must
correspond to the version in the `pyproject.toml` file, except for dev 
releases. The tag for a dev release will be `v<PACKAGE_VERSION>.devN`
where the `.devN` suffix is not part of the package version in the 
`pyproject.toml` file. All tags, except dev releases, should be 
applied to the `main` branch. Dev releases can be applied anywhere
and thus are not guaranteed to be repeatable (e.g., when applied to
a PR that is later merged and the branch is deleted).

Not all [PEP-440](https://peps.python.org/pep-0440/)
tags are supported at this time.

The following steps are required to create a release:
  1. Push a properly formatted tag (vX.Y.Z[aN][.devN]). 
  2. Use the specified tag to create a release

The publish action can also be triggered on a branch through
the UI. In this case, it will use the package version at the
head of the branch.


## Roadmap

See the [open issues](https://github.com/agntcy/acp-sdk/issues) for a list of proposed features and known issues.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**. For detailed contributing guidelines, please see [CONTRIBUTING.md](https://github.com/agntcy/acp-sdk/blob/main/docs/CONTRIBUTING.md).


## Copyright Notice

[Copyright Notice and License](./LICENSE.md)

Distributed under Apache 2.0 License. See LICENSE for more information.
Copyright AGNTCY Contributors (https://github.com/agntcy)

## Acknowledgements

This SDK is developed with the support of the IoA community with the goal of facilitating cross-framework agent interoperability.
