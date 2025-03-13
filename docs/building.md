# Building the packages

## Prerequisites

This repo uses the following tools to build (or update) the packages:
  * yq: to parse OpenAPI yaml
  * make: to store command recipes
  * docker: to run the [openapi-generator-cli](https://github.com/OpenAPITools/openapi-generator-cli) tool
  * git: to checkout the source specifications

## Generating the clients from the OpenAPI ACP specification

