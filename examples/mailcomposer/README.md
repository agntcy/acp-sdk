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

## Environment Variables

Make sure to set the following environment variable:

- `AZURE_OPENAI_API_KEY`: Your API key for accessing Azure OpenAI services (.env file in current folder).

## Install Dependencies

Use Poetry to install the required dependencies:
```bash
poetry install
poetry shell
pip install -U "langgraph-cli[inmem]"
```

## Configure Environment

Ensure that the AZURE_OPENAI_API_KEY environment variable is set. You can set it in your terminal session like so:
```bash
export AZURE_OPENAI_API_KEY="your-api-key-here"
```

## Running the Email Agent using LangGraph Server

To start the email agent, run the following commands.

```bash
poetry shell
langgraph dev
```

Interaction with email agent via:
- 🚀 API: http://127.0.0.1:2024
- 🎨 Studio UI: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
- 📚 API Docs: http://127.0.0.1:2024/docs
