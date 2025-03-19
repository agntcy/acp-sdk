# Email Reviewer (LlamaIndex)

A simple agent written in LlamaIndex (using a `Workflow`) in charge of reviewing and correcting an email

## Agent Input
- `email`: (str) Email to review
- `audience`: (str) one of `general`, `technical`, `business`, `academic`

## Agent Output
- `correct`: (bool) If given email does not contain writing errors and it targets the audience correctly.
- `corrected_email`: (opt, str) The corrected email

## Requirements

 - LlamaIndex: https://docs.llamaindex.ai/en/stable/getting_started/installation/

## Agent local deployment

1) Copy and adapt `.env`: `cp .env.example .env`
1) Install llama-deploy: `pip install llama_deploy`
1) Run apiserver:
    - `python -m llama_deploy.apiserver`
    OR
    - (docker): `docker run -p 4501:4501 -v .:/opt/quickstart -w /opt/quickstart llamaindex/llama-deploy:main`
1) Create deployment config from template: `sed "s|\${PWD}|$(pwd)|g" "email_reviewer.tmpl.yaml" > "email_reviewer.yaml"`
1) Deploy the workflow: `llamactl deploy email_reviewer.yaml`

## Test agent

You can use `usage_example.py` to use the Llama Client SDK to call the agent with given inputs (see source code):
`python usage_example.py `

