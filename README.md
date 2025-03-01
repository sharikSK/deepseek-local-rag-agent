
# **DeepSeek RAG Agent**  

A **local RAG (Retrieval-Augmented Generation) reasoning agent** powered by **DeepSeek R1**, **LangChain**, and **Qdrant** for document-based chat interactions.  

---

## **Prerequisites**  
Before we begin, ensure you have the following installed and ready:  

✅ **Python** (Version **3.10 or higher** recommended)  
✅ **Ollama** installed on your machine  
✅ **Qdrant Cloud** API key (for RAG mode)  
✅ **Exa AI API key** (optional, for web search)  
✅ **A code editor** (Recommended: **VS Code** or **PyCharm**)  
✅ **Basic familiarity with Python programming**  

---

## **Installation & Setup**  

### **1️⃣ Ollama Setup**  
**Step 1:** Install Ollama (Follow [Ollama’s official guide](https://ollama.ai/))  

**Step 2:** Pull the required models:  

- **DeepSeek R1 Models:**  
  - For the **lighter** model:  
    ```bash
    ollama pull deepseek-r1:1.5b
    ```
  - For the **more capable** model (requires better hardware):  
    ```bash
    ollama pull deepseek-r1:7b
    ```

- **Snowflake Arctic Embed Model:**  
  ```bash
  ollama pull snowflake-arctic-embed
  ```

- **Llama 3.2 Model (for Web Search Agent):**  
  ```bash
  ollama pull llama3.2
  ```

---

### **2️⃣ Qdrant Cloud Setup (for RAG Mode)**  
**Step 1:** Visit [Qdrant Cloud](https://cloud.qdrant.io)  

**Step 2:** Sign up or log in  

**Step 3:** Create a new **cluster**  

**Step 4:** Get your API credentials:  
- **Qdrant API Key:** Found in the "API Keys" section  
- **Qdrant URL:** Your cluster URL (format: `https://xxx-xxx.cloud.qdrant.io`)  

---

### **3️⃣ Exa AI API Key (Optional for Web Search)**  
**Step 1:** Visit [Exa AI](https://exa.ai)  

**Step 2:** Sign up for an account  

**Step 3:** Generate an **API key** from your account settings  

---

## **Running the Application**  

1. **Clone the repository:**  
   ```bash
   git clone https://github.com/yourusername/deepseek-rag-agent.git
   cd deepseek-rag-agent
   ```

2. **Install dependencies:**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app:**  
   ```bash
   streamlit run deepseek_rag_agent.py
   ```

---

## **Features**  
✅ **PDF & Web Content Processing** – Upload and analyze documents or web content  
✅ **Retrieval-Augmented Generation (RAG)** – Leverages Qdrant for better context retrieval  
✅ **Custom Agents** – Web search agent (optional) powered by Exa AI  
✅ **Multi-Model Support** – Use **DeepSeek R1**, **Llama3.2**, and **Snowflake Arctic Embed**  
✅ **Streamlit UI** – User-friendly chat interface  

---

## **Contributing**  
We welcome contributions! Feel free to **fork** the repository, **open issues**, and submit **pull requests**.  

---

This version is **clear, structured, and professional** while maintaining **readability**. Let me know if you'd like any modifications! 🚀
