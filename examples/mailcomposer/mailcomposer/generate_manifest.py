from agntcy_acp.manifest import *
from pydantic import TypeAdapter
from state import AgentState, OutputState, ConfigSchema


manifest = AgentManifest(
    metadata=AgentMetadata(
        ref=AgentRef(name="org.agntcy.mailcomposer", version="0.0.1"),
        description="Offer a chat interface to compose an email for a marketing campaign. Final output is the email that could be used for the campaign"),
    specs=AgentACPSpec(
        input=TypeAdapter(AgentState).json_schema(),
        output=TypeAdapter(OutputState).json_schema(),
        config=TypeAdapter(ConfigSchema).json_schema(),
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
                framework_config=LangGraphConfig(
                    framework_type="langgraph",
                    graph="mailcomposer.mailcomposer:graph"
                )
            )
        ],
        dependencies=[]
    )
)

with open("../deploy/mailcomposer.json", "w") as f:
    f.write(manifest.model_dump_json(
        exclude_unset=True,
        exclude_none=True,
        indent=2
    ))