Before we begin, make sure you have the following:

Python installed on your machine (version 3.10 or higher is recommended)

Ollama installed

Your Qdrant and Exa AI (optional) API key

A code editor of your choice (we recommend VS Code or PyCharm for their excellent Python support)

Basic familiarity with Python programming

Initial setup and API keys:

Ollama Setup

Install Ollama

Pull the Deepseek r1 model(s):

For the lighter model
 ollama pull deepseek-r1:1.5b 

For the more capable model (if your hardware supports it)
ollama pull deepseek-r1:7b

Pull Snowflake Arctic Enbed model
ollama pull snowflake-arctic-embed

Pull Llama 3.2 model
ollama pull llama3.2

Qdrant Cloud Setup (for RAG Mode)

Visit Qdrant Cloud

Create an account or sign in

Create a new cluster

Get your credentials:

Qdrant API Key: Found in API Keys section

Qdrant URL: Your cluster URL (format: https://xxx-xxx.cloud.qdrant.io)

Exa AI API Key (Optional)

Visit Exa AI

Sign up for an account

Generate an API key
