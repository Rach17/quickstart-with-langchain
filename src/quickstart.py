import os
from langchain_cohere.llms import Cohere
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Access the Hugging Face API key from the .env file
api_key = os.getenv("COHERE_API_KEY")

# Initialize Cohere LLM
llm = Cohere(temperature=0.7)

# Use the LLM to generate a response
prompt = "Explain LangChain in simple terms."
response = llm.invoke(prompt)

print("Prompt: " + prompt)
print("AI Response:")
print(response)
