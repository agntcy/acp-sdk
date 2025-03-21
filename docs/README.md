# Agent Connect Protocol SDK

## Getting Started

Prerequisites:
  * [poetry](https://python-poetry.org/docs/): for package management

## Usage

Learn how to use the SDK here: [usage](usage#usage)

## Generate generic server

`make generate_acp_server`

Generate a FastAPI server based on the ACP specification.
This is a generic client, because schemas for input, output, and configurations are generic objects, i.e. they are not the specific ones supported by a given agent.

## ACP SDK CLI

```
$ cd agtncy_acp
$ poetry run acp --help
Usage: acp [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  generate-agent-models    Generate pydantic models from agent manifest or
                           descriptor.
  generate-agent-oapi      Generate OpenAPI Spec from agent manifest or
                           descriptor
  validate-acp-descriptor  Validate agent ACP descriptor
  validate-acp-manifest    Validate agent manifest
```
