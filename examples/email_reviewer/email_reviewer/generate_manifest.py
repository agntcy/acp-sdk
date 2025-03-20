
from agntcy_acp.manifest import *
from pydantic import TypeAdapter
from state import EmailReviewerInput, EmailReview,ConfigSchema

manifest = AgentManifest(
    metadata=AgentMetadata(
        ref=AgentRef(name="org.agntcy.mail_reviewer", version="0.0.1"),
        description="Review emails"),
    specs=AgentACPSpec(
        input=EmailReviewerInput.model_json_schema(),
        output=EmailReview.model_json_schema(),
        config=ConfigSchema.model_json_schema(),
        capabilities=Capabilities(
            threads=False,
            callbacks=False,
            interrupts=False
        )
    ),
    deployment=AgentDeployment(
        deployment_options=[
            SourceCodeDeployment(
                type="source_code",
                name="source_code_local",
                url="file://../",
                framework_config=LlamaIndexConfig(
                    framework_type="llamaindex",
                    name="./email_reviewer",
                    path="email_reviewer:email_reviewer_workflow"
                )
            )
        ],
        dependencies=[]
    )
)

with open("../deploy/email_reviewer.json", "w") as f:
    f.write(manifest.model_dump_json(
        exclude_unset=True,
        exclude_none=True,
        indent=2
    ))