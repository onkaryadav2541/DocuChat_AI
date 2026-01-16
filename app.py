import streamlit as st
import os
import shutil
from src.pdf_handler import process_document
from src.vector_store import get_vectorstore
from src.rag_engine import ask_bot # Import the new brain
import src.config

st.set_page_config(page_title="DocuChat AI", page_icon="🤖", layout="wide")

st.title("🤖 DocuChat AI")

# --- SIDEBAR (Ingestion) ---
with st.sidebar:
    st.header("📂 Knowledge Base")
    uploaded_files = st.file_uploader("Upload PDFs", type="pdf", accept_multiple_files=True)
    
    if st.button("Build Brain 🧠"):
        if uploaded_files:
            st.info("🚀 Processing...")
            all_chunks = []
            
            # Temp folder
            if not os.path.exists("temp_docs"):
                os.makedirs("temp_docs")
            
            # Progress bar
            progress_text = "Operation in progress. Please wait."
            my_bar = st.progress(0, text=progress_text)
            
            for i, file in enumerate(uploaded_files):
                temp_path = os.path.join("temp_docs", file.name)
                with open(temp_path, "wb") as f:
                    f.write(file.getbuffer())
                
                chunks = process_document(temp_path)
                all_chunks.extend(chunks)
                my_bar.progress((i + 1) / len(uploaded_files))
            
            # Build Vector Store
            get_vectorstore(all_chunks)
            
            st.success("✅ Brain Built! You can now chat.")
            shutil.rmtree("temp_docs")
        else:
            st.warning("⚠️ Please upload a PDF first.")

# --- MAIN CHAT INTERFACE ---

# 1. Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I have read your documents. Ask me anything."}
    ]

# 2. Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 3. Handle User Input
if prompt := st.chat_input("Ask a question about your documents..."):
    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate Answer
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Call the RAG Engine
                response = ask_bot(prompt)
                st.markdown(response)
                
                # Save assistant message
                st.session_state.messages.append({"role": "assistant", "content": response})
                
            except Exception as e:
                st.error(f"Error: {e}")