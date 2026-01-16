from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from src.config import GOOGLE_API_KEY

def ask_bot(user_query):
    """
    Modern RAG Engine using the 'Latest' alias.
    This automatically finds the working stable model for your region.
    """
    
    # 1. Load Local Embeddings
    embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    # 2. Connect to Database
    vectorstore = Chroma(
        persist_directory="./chroma_db",
        embedding_function=embedding_function
    )
    
    # 3. Setup Gemini
    # ✅ FIX: Using 'gemini-flash-latest'
    # This was explicitly found in your check_models.py list.
    llm = ChatGoogleGenerativeAI(
        model="gemini-flash-latest",
        temperature=0.3,
        google_api_key=GOOGLE_API_KEY
    )
    
    # 4. Create the Prompt
    prompt = ChatPromptTemplate.from_template("""
    Answer the following question based only on the provided context:

    <context>
    {context}
    </context>

    Question: {input}
    """)

    # 5. Create the Chain
    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    
    # 6. Run it
    try:
        response = retrieval_chain.invoke({"input": user_query})
        return response["answer"]
    except Exception as e:
        return f"Error: {str(e)}"