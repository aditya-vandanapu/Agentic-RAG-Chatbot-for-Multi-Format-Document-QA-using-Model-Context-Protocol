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
