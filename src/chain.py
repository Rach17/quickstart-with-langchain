import os
from langchain_cohere import ChatCohere
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv()

# Access the Cohere API key from the .env file
api_key = os.getenv("COHERE_API_KEY")

# Initialize Cohere LLM
model = ChatCohere(model="command-r-plus", cohere_api_key=api_key)

# Define the prompt templates
prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")
analysis_prompt = ChatPromptTemplate.from_template("is this a funny joke? {joke}")

# Create the chains
chain = prompt | model | StrOutputParser()
composed_chain = {"joke": chain} | analysis_prompt | model | StrOutputParser()

# Invoke the chains
topic = "bears"
joke_response = chain.invoke({"topic": topic})
analysis_response = composed_chain.invoke({"topic": topic})

# Print the results
print("Joke:")
print(joke_response)
print("\nAnalysis:")
print(analysis_response)