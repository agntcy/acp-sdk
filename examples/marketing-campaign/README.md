poetry run acp generate-agent-models examples/marketing-campaign/manifests/sendgrid.json --output-dir examples/marketing-campaign/src/marketing_campaign --model-file-name sendgrid.py        

poetry run acp generate-agent-models examples/marketing-campaign/manifests/mailcomposer.json --output-dir examples/marketing-campaign/src/marketing_campaign --model-file-name mailcomposer.py

poetry run acp generate-agent-models examples/email_reviewer/deploy/email_reviewer.json --output-dir examples/marketing-campaign/src/marketing_campaign --model-file-name email_reviewer.py
