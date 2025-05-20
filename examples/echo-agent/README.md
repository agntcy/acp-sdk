# Echo Agent

The echo agent simply repeats input to output adding a new
"assistant" message with a limited number of supported
transformations of the last "human" type message:

- to-upper: convert text to upper case
- to-lower: convert text to lower case

The agent is intended to be used for simple test cases where
access to an LLM is either unsupported or undesired. The agent
outputs a deterministic value based on the input to better
support testable outcomes.

It also supports the following configuration:

  * interrupt: when true, echo data as interrupt once, before 
  echoing resume as output

## Prerequisites

Before running the application, ensure you have the following:

- **Python 3.9 or higher**
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

## Running the Echo Agent directly

* Install dependencies,
    ```shell
    uv sync
    ```

* Run the agent CLI using uv,
    ```shell
    export TO_LOWER=true ; uv run -m echo_agent.main --human "What is actually up?"
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

* Create an environment variable file if desired based on the example.

* Make sure that the [workflow server manager](https://docs.agntcy.org/pages/agws/workflow_server_manager.html#getting-started) cli (wfsm) is added to your path.

- Start the workflow server. Note the existing manifest
  assumes you are deploying from the directory with the `pyproject.toml`
  file for the echo agent. Adjust as needed.

If using wfsm version prior to 0.2.1,
  ```shell
  wfsm deploy --manifestPath deploy/echo-agent-manifest.json --envFilePath deploy/echo-agent-wfsm-config.yaml
  ```

Otherwise use,
  ```shell
  wfsm deploy --manifestPath deploy/echo-agent-manifest.json --configPath=deploy/echo-agent-wfsm-config.yaml
  ```

  When the serve is up an running we can make a request to the agent using `curl`. The example below
  uses the defaults:

  ```shell
  curl -s -H 'content-type: application/json' -H "x-api-key: 910ffe03-3aca-48c0-aa40-66ab54bbf79a" -d '{"agent_id": "91b76349-cba0-4e3c-8252-e94fff20de4f", "input": { "messages": [ { "type": "human", "content": "What is up, Dude?" } ] }, "config": { "configurable": { "to_upper": true } } }' http://127.0.0.1:8080/runs/wait
  ```
