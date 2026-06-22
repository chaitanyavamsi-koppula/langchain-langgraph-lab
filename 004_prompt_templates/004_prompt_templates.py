"""
Use a ChatPromptTemplate to rewrite the tone of a customer email,
then run it through Gemini.
"""

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

# Load GOOGLE_API_KEY / GEMINI_API_KEY from a local .env file
load_dotenv()

# Chat model that will run the prompt
model = ChatGoogleGenerativeAI(model="gemini-3.5-flash")

# Plain string (NOT an f-string) so {style} and {text} stay as
# placeholders for LangChain to fill in later via format_messages()
template_string = """Translate the text \
that is delimited by triple backticks \
into a style that is {style}. \
text: ```{text}```
"""

# Reusable prompt template built from the string above
prompt_template = ChatPromptTemplate.from_template(template_string)

# Target tone to translate the email into
customer_style = """American English \
in a calm and respectful tone
"""

# Raw email we want rewritten
customer_email = """
Arrr, I be fuming that me blender lid \
flew off and splattered me kitchen walls \
with smoothie! And to make matters worse, \
the warranty don't cover the cost of \
cleaning up me kitchen. I need yer help \
right now, matey!
"""

# Fill the placeholders — keyword names must match {style} and {text}
customer_messages = prompt_template.format_messages(style=customer_style, text=customer_email)

# Send to the model and print just the text of the reply
response = model.invoke(customer_messages)
print(response.text)
