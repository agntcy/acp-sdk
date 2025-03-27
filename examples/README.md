# How to run our example application locally
Prerequisites:

[Make](https://cmake.org/)

[Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

[Python at lest verstion 3.9](https://www.python.org/downloads/)

[Docker with buildx](https://docs.docker.com/get-started/get-docker/)

[docker-compose](https://docs.docker.com/compose/)

[Golang](https://go.dev/doc/install)

[Git LFS](https://git-lfs.com/)

Clone the repositories 

[ACP SDK](https://github.com/agntcy/acp-sdk/tree/main)

[Workflow server](https://github.com/agntcy/workflow-srv)

[Workflow server manager](https://github.com/agntcy/workflow-srv-mgr)

[API bridge agent](https://github.com/agntcy/api-bridge-agnt)

# Getting started
### Build Workflow server manager 
Navigate to folder wfsm and execute the make build command
```sh
cd wfsm
make build
```
This will create a build folder with the wfsm executable

### Build Workflow server
Build the docker image
```sh
make docker-build-dev
```
### Run API Bridge Agent
Inside the api bridge repository run the following command in the order they appear
```sh
make start_redis
make start_tyk
```
From a separate terminal from within the api bridge agent run 
```sh
curl http://localhost:8080/tyk/apis/oas \
  --header "x-tyk-authorization: foo" \
  --header 'Content-Type: text/plain' \
  -d@configs/api.sendgrid.com.oas.json

curl http://localhost:8080/tyk/reload/group \
  --header "x-tyk-authorization: foo"
```

### Run the example ACP SDK
1. Go to the examples folder by
```sh 
cd examples
```
2. Inside deploy folder you will find a file called marketing_campaign_example.yaml open this file on your editor and make sure the contents 
```yaml
values:
  AZURE_OPENAI_API_KEY: your_secret
  AZURE_OPENAI_ENDPOINT: "the_url.com"
  API_HOST: 0.0.0.0
  SENDGRID_HOST: http://host:port
  SENDGRID_API_KEY: SG.your-api-key
  MAILCOMPOSER_ID: mailcomposer-id
  EMAIL_REVIEWER_ID: email_reviewer_id

dependencies:
  - name: mailcomposer
    values:
      AZURE_OPENAI_API_KEY:  your_secret
      AZURE_OPENAI_ENDPOINT: "the_url.com"
  - name: email_reviewer
    values:
      AZURE_OPENAI_API_KEY: your_secret
      AZURE_OPENAI_ENDPOINT: "the_url.com"
```

3. From within the example folder run
```zsh
../../workflow-srv-mgr/wfsm/build/wfsm deploy -m ./marketing-campaign/deploy/marketing-campaign.json -e ./marketing-campaign/deploy/marketing_campaign_example.yaml -b workflowserver:latest
```
If everything goes well you will have the full application up and running, and in the logs there are a few important information to copy for later steps these are: 
-  Agent ID
- API Key
- Host

Once all is up and running test it by adjusting and running the following curl
```sh
curl --location 'http://localhost:<port>/runs/wait' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'x-api-key: <replace with api-key>' \
--data-raw '{
    "agent_id": "<replace with agent-id>",
    "thread_id": "1",
    "input": {
        "messages": [
            {"type":"human","content":"**************\n\nSubject: March Green Sale\n\nDear [Client'\''s Name],\n\nI hope this message finds you well. We are excited to announce an exclusive offer from our brand, Verdant Vogue, that you won'\''t want to miss!\n\nThis March, we'\''re celebrating the vibrant spirit of spring with a special 20% discount on all our green clothing items. This is the email.\n\nWarm regards,\n\n[Your Full Name]  \n[Your Position]  \nVerdant Vogue  \n[Contact Information]\n**************"
            },
            {
                "content": "OK",
                "type": "human"
            }
        ]
    },
    "metadata": {},
    "config": {
        "configurable":{
            "recipient_email_address": "Jonh Doe <replace with test-email>",
            "sender_email_address": "casey.agntcy.demo@gmail.com",
            "target_audience": "academic"
        }
    }
}
'
```
