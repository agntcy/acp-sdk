# Building the package

The `acp-sdk` Python package is built on GitHub and published using GitHub 
actions. The action can be found in the relevant workflows directory in the 
repo. The project attempts to keep the client SDK updated on any ACP or 
relevant specification changes, but delays can happen.

## Prerequisites

This repo uses the following tools to build (or update) the packages:
  * yq: to parse OpenAPI yaml
  * make: to store command recipes
  * docker: to run the 
  [openapi-generator-cli](https://github.com/OpenAPITools/openapi-generator-cli) tool
  * git: to checkout the source specifications

## Generating the clients from the OpenAPI ACP specification

There are two make targets to generate the clients:
  * `make generate_acp_client`
  * `make generate_acp_async_client`

Note that the make targets add a SPDX header and update the package 
imports to match the files as they should appear in the `acp_sdk/acp_vXX`
subpackages. Please check the Makefile for questions on how this is done.

To update the `acp_sdk` package by copying the relevant files, use: 
`make update_python_subpackage`

## Updating the client package on a new ACP specification release

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
      * `acp_sdk/__init__.py`
      * `acp_sdk/models/__init__.py`
  3. Check for any irregularities: `git diff`
  4. Run: `make test`
