# Quickstart with LangChain

This repository contains a quickstart guide for using LangChain, an open-source library for developing applications powered by large language models (LLMs) and AI tools. The project demonstrates how to interact with language models, integrate them into chains, and utilize memory capabilities for creating advanced AI-driven applications.

## Features

- **Basic Interaction with Cohere LLM:** Demonstrates how to generate responses using the Cohere language model.
- **Chains:** Shows how to create and use LangChain chains for processing and generating structured outputs.
- **Memory:** Implements a conversational chain with memory for maintaining context over multiple interactions.

## Requirements

- Python 3.7+
- Required Python packages listed in `requirements.txt`

## Setup Instructions

### 1. Clone the Repository
First, clone this repository to your local machine:

```bash
git clone https://github.com/Rach17/quickstart-with-langchain.git
cd quickstart-with-langchain
```

### 2. Install Dependencies
Install the required Python libraries using `pip`:

```bash
pip install -r requirements.txt
```

### 3. Set Up API Keys
To interact with the Cohere API, you'll need an API key. Follow these steps:

- Go to [Cohere](https://cohere.ai/) and sign up for an API key.
- Create a `.env` file in the root directory of the project and add your API key like this:

```env
COHERE_API_KEY=your_api_key_here
```

### 4. Run the Scripts

You can run the example scripts to see how LangChain works with Cohere:

- **`quickstart.py`**: Demonstrates basic interaction with the Cohere language model.
- **`chain.py`**: Shows how to use LangChain chains for generating and analyzing jokes.
- **`memory.py`**: Implements a conversational chain that maintains context across interactions.

Run any of the scripts as follows:

```bash
python quickstart.py
```

### 5. Explore the Code

- **`quickstart.py`**: Initializes the Cohere LLM, sends a prompt to the model, and prints the response.
- **`chain.py`**: Defines a chain that generates a joke and then analyzes whether it is funny.
- **`memory.py`**: Implements a conversation where the AI remembers previous queries (maintains context).

## Acknowledgements

- **LangChain**: A powerful framework for LLM-powered applications.
- **Cohere**: Provides powerful, large language models that can be used to generate and understand text.
