from typing import Literal
from pydantic import BaseModel, Field
from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv()


class Review(BaseModel):
    sentiment: Literal["positive", "negative", "neutral"]
    reason: str
    stars: int = Field(ge=1, le=5)


agent = create_agent(
    model="google_genai:gemini-2.5-flash-lite",
    system_prompt="You are a helpful assistant that can analyze reviews and provide a sentiment and stars rating.",
    response_format=Review,
)

review = "Oh, absolutely love it. Broke on day two, support never replied, and I got to buy it twice. Genuinely a five-star experience."

result = agent.invoke(
    {
        "messages": [{"role": "user", "content": review}],
    },
    config={"configurable": {"thread_id": "review_analysis"}},
)

print(result["messages"][-1].content_blocks)
