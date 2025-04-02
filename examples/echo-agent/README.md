# Echo Agent

The echo agent simply repeats input to output adding a new
"assistant" message with a limited number of supported
transformations of the last "human" type message:

  * to-upper: convert text to upper case
  * to-lower: convert text to lower case

The agent is intended to be used for simple test cases where
access to an LLM is either unsupported or undesired. The agent
outputs a deterministic value based on the input to better
support testable outcomes.

## Prerequisites

Before running the application, ensure you have the following:

- **Python 3.9 or higher**
- [Poetry](https://python-poetry.org/)

## Running the Echo Agent directly

* Install dependencies
    ```
    poetry install
    ```

* Run the agent CLI using poetry
    ```
    export TO_LOWER=true ; poetry run echo_agent --human "What is actually up?"
    {
      "messages": [
        {
          "type": "human",
          "content": "What is actually up?"
        },
        {
          "type": "assistant",
          "content": "what is actually up?"
        }
      ]
    }
    ```

## Running the Echo Agent using Agent Workflow Server

* Create an environment variable file if desired based on the example

* Make sure that the [workflow server manager](https://docs.agntcy.org/pages/agws/workflow_server_manager.html#getting-started) cli (wfsm) is added to your path

* Start the workflow server
    ```
    wfsm deploy -m deploy/echo-agent.json -e deploy/echo_agent_example.yaml -b workflowserver:latest
    ```
