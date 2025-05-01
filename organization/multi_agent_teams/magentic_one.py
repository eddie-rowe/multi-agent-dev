# Magentic One 
# A team that runs a group chat with participants managed by the MagenticOneOrchestrator.
# The orchestrator handles the conversation flow, ensuring that the task is completed efficiently 
# by managing the participants’ interactions.
# The orchestrator is based on the Magentic-One architecture, which is a generalist multi-agent 
# system for solving complex tasks.
# https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/teams.html

# Import the necessary libraries
import asyncio
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.teams import MagenticOneGroupChat
from autogen_agentchat.ui import Console
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.agents.web_surfer import MultimodalWebSurfer
from autogen_ext.agents.file_surfer import FileSurfer
from autogen_ext.agents.magentic_one import MagenticOneCoderAgent
from autogen_agentchat.agents import CodeExecutorAgent
from autogen_ext.code_executors.local import LocalCommandLineCodeExecutor

# Define the main function
async def main() -> None:
    
    # Initialize the model client 
    model_client = OpenAIChatCompletionClient(model="gpt-4o")

    # Initialize the agents
    surfer = MultimodalWebSurfer(
        "WebSurfer",
        model_client=model_client,
    )
    file_surfer = FileSurfer(
         "FileSurfer",
         model_client=model_client
    )
    coder = MagenticOneCoderAgent(
        "Coder",
        model_client=model_client
    )
    terminal = CodeExecutorAgent(
        "ComputerTerminal",
        code_executor=LocalCommandLineCodeExecutor()
    )
    assistant = AssistantAgent(
        "Assistant",
        model_client=model_client,
    )

    # Initialize the team
    team = MagenticOneGroupChat([surfer, file_surfer, coder, terminal, assistant], model_client=model_client)

    # Run the team
    await Console(team.run_stream(task="What is the UV index in Melbourne today?"))

# Run the main function
asyncio.run(main())