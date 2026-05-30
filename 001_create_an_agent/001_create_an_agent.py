from dotenv import load_dotenv
from langchain.agents import create_agent

load_dotenv()


# get_weather function is used to get weather information for a given city
def get_weather(city: str) -> str:
    """
    Get weather for a given city.

    :param city: takes city as input
    :type city: str
    :return: returns weather_info in the provided city
    :rtype: str
    """
    return f"It's always sunny in {city}!"


agent = create_agent(
    model="google_genai:gemini-2.5-flash-lite",
    tools=[get_weather],
    system_prompt="you are a helpful assistant",
)

result = agent.invoke(
    {
        "messages": [
            {"role": "user", "content": "What's is the weather like in san fransisco"}
        ]
    }
)

print(result["messages"][-1].content_blocks)
