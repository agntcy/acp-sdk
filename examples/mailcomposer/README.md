# Compose Email Agent

The Compose Email Agent is built using LangGraph to facilitate interactive email composition.
It collects email details by continuously interacting with the user until tha latter confirm that the email is ready, then provides the finalized email text.

## Features

- Utilizes Azure OpenAI to guide email composition.
- Demonstrates the use of LangGraph for managing conversational state and flow.
- Provides a LangGraph server setup for interacting via ACP protocol APIs.

## Prerequisites

Before running the application, ensure you have the following:

- **Azure OpenAI API Key**: Set up as an environment variable.
- **Poetry**: A tool for dependency management and packaging in Python.



## Running the Email Agent using Agent Workflow Server

* Create an environment variable file with the following data:
    ```commandline
    echo "
    AZURE_OPENAI_MODEL=gpt-4o-mini
    AZURE_OPENAI_API_KEY=***YOUR_OPENAI_API_KEY***
    AZURE_OPENAI_ENDPOINT=https://smith-project-agents.openai.azure.com
    OPENAI_API_VERSION=2024-07-01-preview 
    API_HOST=0.0.0.0
    " > deploy/.mailcomposer.env
    ```
* Make sure that the workflow server manager cli (`wfsm`) is added to your path
* Start the workflow server
    ```
    cd deploy;
    wfsm deploy -m ./mailcomposer.json -e .mailcomposer.env
    ```


