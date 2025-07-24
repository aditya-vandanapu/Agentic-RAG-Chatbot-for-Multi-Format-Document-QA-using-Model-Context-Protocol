# 🤖 Agentic RAG Chatbot 📚  
**Multi-Format Document Q&A using Agent-based Retrieval-Augmented Generation and MCP**

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-%E2%9D%A4-red?logo=streamlit)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5--Turbo-green?logo=openai)
![LangChain](https://img.shields.io/badge/LangChain-RAG-yellow)

---

## 🔍 Overview

A modular AI chatbot to answer questions from uploaded documents using:

- 🧠 **GPT-3.5-Turbo via OpenAI**
- 🔍 **LangChain + FAISS for Retrieval**
- 🗂️ **Multi-format support:** PDF, DOCX, TXT, CSV, PPTX
- 🧩 **Agent-based architecture**:
  - `IngestionAgent` → Parses & Chunks docs
  - `RetrievalAgent` → Retrieves context from vector DB
  - `LLMResponseAgent` → GPT-powered answer generator
- 🔄 **MCP (Message Carrier Protocol)** → Traceable, explainable message flow
- 💻 **Streamlit UI**

---

## 💻 How to Run

### 📦 1. Install dependencies

```bash
pip install -r requirements.txt
🔑 2. Setup .env file
env
Copy code
OPENAI_API_KEY=your_openai_key_here
▶️ 3. Start Streamlit App
bash
Copy code
streamlit run app.py
🧠 Architecture
mermaid
Copy code
flowchart TD
    A[📤 User Uploads Files] --> B[🧩 IngestionAgent<br>→ Parse + Chunk]
    B --> C[📚 RetrievalAgent<br>→ Retrieve Relevant Chunks]
    C --> D[🧠 LLMResponseAgent<br>→ Answer with GPT-3.5]
    D --> E[✅ Final Answer + Trace Logs (MCP)]
📸 Screenshots
Upload & Embed	Chat Response	Logs

⚙️ Tech Stack
Python

Streamlit

OpenAI GPT-3.5

LangChain

FAISS

dotenv

MCP-style agent communication

🧩 Modular Agents
Agent	Role
IngestionAgent	Loads + splits docs
RetrievalAgent	Finds relevant chunks
LLMResponseAgent	Uses GPT to generate answers
utils.mcp.py	Handles message passing

🧠 Challenges
Aligning chunk format across formats (CSV, PPTX, PDFs)

Handling longer context tokens with OpenAI API

Ensuring fast FAISS retrieval

Maintaining clean agent boundaries

🚀 Future Scope
Add support for image OCR PDFs

Integrate open-source LLMs via Ollama

Use async agents for performance

Add chat history saving

👨‍💻 Author
Aditya Vandanapu


