import streamlit as st

# Streamlit App Initialization
st.title("Deepseek Local RAG Reasoning Agent")

# Session State Initialization
if 'google_api_key' not in st.session_state:
    st.session_state.google_api_key = ""
if 'qdrant_api_key' not in st.session_state:
    st.session_state.qdrant_api_key = ""
if 'qdrant_url' not in st.session_state:
    st.session_state.qdrant_url = ""
if 'model_version' not in st.session_state:
    st.session_state.model_version = "deepseek-r1:1.5b"  # Default to lighter model
if 'vector_store' not in st.session_state:
    st.session_state.vector_store = None
if 'processed_documents' not in st.session_state:
    st.session_state.processed_documents = []
if 'history' not in st.session_state:
    st.session_state.history = []
if 'exa_api_key' not in st.session_state:
    st.session_state.exa_api_key = ""
if 'use_web_search' not in st.session_state:
    st.session_state.use_web_search = False
if 'force_web_search' not in st.session_state:
    st.session_state.force_web_search = False
if 'similarity_threshold' not in st.session_state:
    st.session_state.similarity_threshold = 0.7
if 'rag_enabled' not in st.session_state:
    st.session_state.rag_enabled = True  # RAG is enabled by default

# Sidebar Configuration
st.sidebar.header("🤖 Agent Configuration")
st.sidebar.header("📦 Model Selection")
model_help = """
- 1.5b: Lighter model, suitable for most laptops
- 7b: More capable but requires better GPU/RAM
"""
st.session_state.model_version = st.sidebar.radio(
    "Select Model Version",
    options=["deepseek-r1:1.5b", "deepseek-r1:7b"],
    help=model_help
)

st.session_state.rag_enabled = st.sidebar.toggle("Enable RAG Mode", value=st.session_state.rag_enabled)

if st.session_state.rag_enabled:
    st.sidebar.header("🔑 API Configuration")
    qdrant_api_key = st.sidebar.text_input("Qdrant API Key", type="password")
    qdrant_url = st.sidebar.text_input("Qdrant URL")

# Chat Interface
chat_col, toggle_col = st.columns([0.9, 0.1])
with chat_col:
    prompt = st.chat_input("Ask about your documents..." if st.session_state.rag_enabled else "Ask me anything...")
with toggle_col:
    st.session_state.force_web_search = st.toggle('🌐', help="Force web search")

if prompt:
    st.session_state.history.append({"role": "user", "content": prompt})
    # Further logic for processing chat input
