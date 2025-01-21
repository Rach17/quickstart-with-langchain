# Quickstart with LangChain

This repository provides a quickstart guide for using LangChain, a powerful library for building applications with large language models (LLMs). The project demonstrates how to integrate with Cohere's LLM, build chains, and maintain memory within conversations using LangChain.

## Features

- **Basic Interaction with Cohere LLM**: Generate responses using Cohere's language model.
- **Chains**: Demonstrate the creation and use of LangChain chains to process and generate outputs.
- **Memory**: Implement conversational chains that maintain context across multiple interactions.

## Requirements

- Python 3.7+
- Virtual Environment

### Required Python Packages

The following Python packages are required to run the project:

- `langchain==0.3.14`
- `langchain-core==0.3.30`
- `langchain-cohere==0.3.4`
- `python-dotenv==1.0.1`

## Setup Instructions

### 1. Clone the Repository
Clone this repository to your local machine:

```bash
git clone https://github.com/Rach17/quickstart-with-langchain.git
cd quickstart-with-langchain
```

### 2. Create a Virtual Environment

#### For Windows:
```bash
python -m venv langchainenv
```

#### For macOS/Linux:
```bash
python3 -m venv langchainenv
```

### 3. Activate the Virtual Environment

#### For Windows:
```bash
.\langchainenv\Scripts\activate
```

#### For macOS/Linux:
```bash
source langchainenv/bin/activate
```

Once the environment is activated, your prompt should show `(langchainenv)` indicating you're in the virtual environment.

### 4. Install Dependencies
With the virtual environment activated, install the required dependencies:

```bash
pip install -r requirements.txt
```

### 5. Set Up API Keys
To interact with the Cohere API, you'll need an API key. Follow these steps:

- Sign up for an API key at [Cohere](https://cohere.ai/).
- Create a `.env` file in the root directory of the project and add your API key:

```env
COHERE_API_KEY=your_api_key_here
```

### 6. Run the Scripts

You can now run the example scripts to see how LangChain works with Cohere:

- **`quickstart.py`**: Demonstrates basic interaction with the Cohere language model.
- **`chain.py`**: Shows how to create chains for generating and analyzing jokes.
- **`memory.py`**: Implements a conversational chain that maintains context over multiple interactions.

Run any of the scripts as follows:

```bash
python quickstart.py
```

### 7. Explore the Code

- **`quickstart.py`**: Initializes the Cohere LLM, sends a prompt to the model, and prints the response.
- **`chain.py`**: Defines a chain to generate a joke and analyze whether it is funny.
- **`memory.py`**: Implements a conversation chain that remembers previous queries.

## Contributing

We welcome contributions! If you'd like to improve this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -am 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new Pull Request.

Please ensure that your changes do not break existing functionality and include tests where appropriate.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **LangChain**: A powerful framework for building LLM-powered applications.
- **Cohere**: Provides large language models that can be used to generate and understand text.
