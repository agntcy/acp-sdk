# Agent Connect Protocol SDK

## Getting Started

## Usage

Learn how to use the SDK here: [usage](usage#usage)

## Generate genericeserver

`make generate_acp_server`

Generate a FastAPI server based on the ACP specification.
This is a generic client, because schemas for input, output, and configurations are generic objects, i.e. they are not the specific ones supported by a given agent.

## ACP SDK CLI

```
cd acp-sdk
poetry run acp --help

Usage: acp [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  generate-agent-oapi
  validate-acp-descriptor
```
