from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient


# Get the OpenAI model from the environment variable
openai_model = os.environ["OPENAI_MODEL"]

# Create an OpenAI model client
model_client = OpenAIChatCompletionClient(
    model=openai_model,
    # api_key is taken from local environment variable OPENAI_API_KEY
)

# Define a function/tool that returns the weather for a given city
async def get_weather(city: str) -> str:
    """Get the weather for a given city."""
    return f"The weather in {city} is 73 degrees and Sunny."


# Define an AssistantAgent with the model, function/tool, system message, and reflection enabled.
# The system message instructs the agent via natural language.
agent = AssistantAgent(
    name="weather_agent",
    model_client=model_client,
    tools=[get_weather],
    system_message="You are a helpful assistant.",
    reflect_on_tool_use=True,
    model_client_stream=True,  # Enable streaming tokens from the model client.
)

# Run the agent and stream the messages to the console.
await Console(agent.run_stream(task="What is the weather in New York?"))