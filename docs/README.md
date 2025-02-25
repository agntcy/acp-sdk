# Agent Connect Protocol SDK

## Getting Started

### Clone and update submodules
```sh
git submodule update --init --recursive
```

### Install project dependencies

```sh
cd acp-sdk
poetry install
```

### Generate generic clients and servers
#### Generate generic client 

`make generate_acp_client`

Generate a python client to consume the ACP specification. 
This is a generic client, because schemas for input, output, and configurations are generic objects, i.e. they are not the specific ones supported by a given agent.

To generate a client for a specific agent check the SDK CLI.


#### Generate genericeserver

`make generate_acp_server`

Generate a FastAPI server based on the ACP specification.
This is a generic client, because schemas for input, output, and configurations are generic objects, i.e. they are not the specific ones supported by a given agent.

### ACP SDK CLI

```
cd acp-sdk
poetry run acp --help

Usage: acp [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  generate-agent-client
  generate-agent-models
  generate-agent-oapi
  validate-manifest
```
