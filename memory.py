import os
from langchain_cohere.llms import Cohere
from dotenv import load_dotenv
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

# Load environment variables
load_dotenv()

# Access the Cohere API key from the .env file
api_key = os.getenv("COHERE_DEFAULT_API_KEY")

# Initialize Cohere LLM
llm = Cohere()


# Initialize memory
memory = ConversationBufferMemory()

# Create a conversation chain
conversation = ConversationChain(llm=llm, memory=memory)

# Start a conversation
response = conversation.invoke("Hi, who won the 2022 FIFA World Cup?")
print(response)

response = conversation.invoke("What about the 2018 winner?")
print(response)