import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import streamlit as st
from agents.ingestion_agent import IngestionAgent
from agents.retrieval_agent import RetrievalAgent
from agents.llm_response_agent import LLMResponseAgent
from utils.mcp import pretty_print_mcp

st.set_page_config(page_title="Agentic RAG Chatbot", layout="wide")
st.title("📚 Agentic RAG Chatbot with MCP")

# Initialize retriever and chat memory
if "retriever" not in st.session_state:
    st.session_state.retriever = RetrievalAgent()
    st.session_state.chat_history = []

# File uploader
uploaded_files = st.file_uploader(
    "Upload files",
    type=["pdf", "pptx", "csv", "docx", "txt", "md"],
    accept_multiple_files=True
)

# Handle ingestion
if uploaded_files:
    ingestor = IngestionAgent()
    mcp_ingest = ingestor.run(uploaded_files)
    st.session_state.retriever.embed_chunks(mcp_ingest["payload"]["chunks"])
    st.success("✅ Documents parsed and embedded!")

# Ask a question
query = st.text_input("Ask a question")
if st.button("Ask") and query:
    mcp_retrieval = st.session_state.retriever.retrieve(query)
    llm_agent = LLMResponseAgent()
    mcp_final = llm_agent.generate_response(
        mcp_retrieval["payload"]["retrieved_context"], query
    )

    st.session_state.chat_history.append({
        "q": query,
        "a": mcp_final["payload"]["answer"]
    })

    # Display final answer
    st.subheader("🧠 Answer")
    st.write(mcp_final["payload"]["answer"])

    # Show source chunks
    with st.expander("📄 Source Chunks"):
        for chunk in mcp_final["payload"]["source"]:
            st.markdown(f"**{chunk['source']} - {chunk['location']}**")
            st.info(chunk["content"])

    # Trace logs (MCP message trace)
    with st.expander("🪵 Trace Logs (MCP Messages)"):
        st.code(pretty_print_mcp(mcp_retrieval), language="json")
        st.code(pretty_print_mcp(mcp_final), language="json")

    # Chat history
    with st.expander("💬 Chat History"):
        for h in st.session_state.chat_history:
            st.markdown(f"**Q:** {h['q']}")
            st.markdown(f"**A:** {h['a']}")
