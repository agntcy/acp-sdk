import json

from langchain_core.messages import AIMessage, HumanMessage
from dotenv import load_dotenv, find_dotenv

load_dotenv(dotenv_path=find_dotenv(usecwd=True))
from mailcomposer.mailcomposer import graph, AgentState, OutputState

def main():
    output = OutputState(
        messages=[],
        final_email=None
    )
    while(True) :
        if len(output["messages"]) > 0:
            m = output["messages"][-1]
            print(f"[Assistant] \t\t>>> {m.content}")
        if "final_email" in output and output["final_email"]:
            break
        message = input("YOU [Type OK when you are happy with the email proposed] >>> ")

        nextinput = AgentState(
            messages = output["messages"] + [HumanMessage(content=message)]
        )
        if message == "OK":
            nextinput["is_completed"] = True
        output:OutputState = graph.invoke(nextinput, {"configurable": {"thread_id": "foo"}})

    print("Final email is:")
    print(output["final_email"])

main()
             