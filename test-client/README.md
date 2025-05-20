# Test client for ACP SDK client

## Usage

Usage: cli [OPTIONS] TEST_INPUT_FILENAME

Options:

    --async / --no-async            Use the async API client.
    --env TEXT                      Override environment variable with format:
                                    "name=value" Can be specified multiple
                                    times.
    --log-level [critical|error|warning|info|debug]
                                    Set logging level.
    --help                          Show this message and exit.

## Running examples

The `test-client/examples/` directory contains example test 
configurations. The following guide uses the Echo
Agent from the `examples/echo-agent/` directory in this repo. Note
that all commands in this example are run with paths relative to the 
root level of this repository.

  1. Make sure that the [workflow server manager](https://docs.agntcy.org/pages/agws/workflow_server_manager.html#getting-started) cli (wfsm) is added to your path.

  2. Start the echo agent using the workflow server 
  manager.

  ```shell
  cd examples/echo-agent ; wfsm deploy --manifestPath deploy/echo-agent-manifest.json --configPath deploy/echo-agent-wfsm-config.yaml --dryRun=false
  ```

  3. Configure the test variables to match the server
  deployment. These can be stored in a `.env` file or
  supplied on the command line. The `test-client/.env.example` file 
  contains settings matching the supplied default config for the echo-agent
  in `examples/echo-agent/deploy/echo-agent-wfsm-config`.

  4. Run the test async client from the CLI on the stateless API set.

  ```shell
  cd test-client ; uv sync && uv run cli --async ./examples/echo_agent_stateless.yaml
  ```

  5. Run the test sync client from the CLI on the stateful API set.

  ```shell
  cd test-client ; uv sync && uv run cli ./examples/echo_agent_stateful.yaml
  ```

## Test configuration file layout

The configuration file has two sections: `metadata` and `operations`.

### Test metadata

The test metadata allows you to set the API client configuration:

  * client_config: an agntcy_acp.ApiClientConfiguration object
  * env_prefix: a string to get values from corresponding environment 
  variables where the names are prefix + parameter name.

    For example, with env_prefix="TEST_", the test-client would look
    for the agent endpoint in "TEST_ENDPOINT".


### Test operations

This is a list of operations that are executed in order. Each
operation is defined by the endpoint ID from the ACP OpenAPI 
specification and the necessary arguments.

The YAML is evaluated as a [Jinja template](https://jinja.palletsprojects.com/en/stable/) with the following render
context:

  * env: the environment variables of the CLI process
  * results: a list of the results of previous operations

For example, the following operation will create a run when the
environment is correctly specified:

```yaml
  - operation_id: create_stateless_run
    test_input:
      run_create_stateless:
        type: agntcy_acp.models.RunCreateStateless
        arguments:
          agent_id: "{{ env.ECHO_AGENT_AGENT_ID }}"
          input:
            messages:
              - type: human
                content: "What is up, Dude?"
          config:
            configurable:
              to_upper: true
    output_at_least:
      status: pending
```

If the next run wants to use the run_id produced by this create operation,
it can use the results context:

```yaml
  - operation_id: get_stateless_run
    test_input:
      run_id:
        type: str
        value: "{{ results[-1].run_id }}"
    output_at_least:
      status: success
```

Success is considered if the API call does not have an exception, and if 
the output match is specified and met. The currently supported matches are:

  * output_at_least: the result object should contain at least the properties
  and values specified. Additional properties in the result are ignored, but
  missing properties are considered an error.
  * output_exact: the result object should match exactly as specified. Note
  that datetime objects are ignored so that for example, the `created_at` field
  of the `Run` response object is ignore.

> [!NOTE]
> Objects must match the structure of the models in agntcy_acp.models
