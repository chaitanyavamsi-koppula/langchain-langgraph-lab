from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

customer_review = """\
This leaf blower is pretty amazing.  It has four settings:\
candle blower, gentle breeze, windy city, and tornado. \
It arrived in two days, just in time for my wife's \
anniversary present. \
I think my wife liked it so much she was speechless. \
So far I've been the only one using it, and I've been \
using it every other morning to clear the leaves on our lawn. \
It's slightly more expensive than the other leaf blowers \
out there, but I think it's worth it for the extra features.
"""

review_template = """\
For the following text, extract the following information:

gift: Was the item purchased as a gift for someone else? \
Answer True if yes, False if not or unknown.

delivery_days: How many days did it take for the product \
to arrive? If this information is not found, output -1.

price_value: Extract any sentences about the value or price,\
and output them as a comma separated Python list.

text: {text}
"""

class Review(BaseModel):
    gift: bool = Field(description="Was the item purchased as a gift for someone else?")
    delivery_days: int = Field(description="How many days did it take for the product to arrive? If this information is not found, output -1.")
    price_value: list[str] = Field(description="Extract any sentences about the value or price, and output them as a comma separated Python list.")

prompt = ChatPromptTemplate.from_template(review_template)

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash")

structured_model = model.with_structured_output(Review)

chain = prompt | structured_model

result = chain.invoke({"text": customer_review})

print(type(result))
