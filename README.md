# 🤖 DocuChat AI

> **A Hybrid RAG (Retrieval-Augmented Generation) Application** that enables secure, cost-effective chat with your PDF documents.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=LangChain&logoColor=white)
![Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=Google%20Gemini&logoColor=white)

---

## 📖 Overview

**DocuChat AI** allows users to upload multiple PDF documents and ask questions in natural language. The system provides accurate, context-aware answers by referencing the specific content of your files.

Unlike standard wrappers, this project utilizes a **Hybrid Architecture** for maximum efficiency:
1.  **Local "Brain" (Privacy & Cost):** Uses `HuggingFace` embeddings running locally on your CPU. This ensures your data structure remains private and you pay **$0** in embedding costs.
2.  **Cloud "Genius" (Speed & Intellect):** Uses **Google Gemini Flash** for high-speed answer generation, utilizing smart routing to find the most stable model available in your region.

---

## 🚀 Key Features

-   **Zero-Cost Embeddings:** Powered by `sentence-transformers/all-MiniLM-L6-v2` (Running locally).
-   **Smart Model Routing:** Automatically detects and switches to the best available Google Gemini model (`gemini-flash-latest`) to bypass regional restrictions.
-   **Persistent Memory:** Your "Brain" (`./chroma_db`) is saved to disk, so you don't have to re-process documents every time you restart.
-   **Multi-File Ingestion:** Upload and process multiple PDFs simultaneously.
-   **Rate-Limit Protection:** Built-in "Stubborn Retry" logic and batching to prevent API crashes on the Free Tier.

---

## 🛠️ Tech Stack

-   **Frontend:** [Streamlit](https://streamlit.io/)
-   **Orchestration:** [LangChain](https://www.langchain.com/) (Modern LCEL Architecture)
-   **Vector Database:** [ChromaDB](https://www.trychroma.com/)
-   **LLM:** Google Gemini 1.5 Flash / Pro (via `langchain-google-genai`)
-   **Embeddings:** HuggingFace (`all-MiniLM-L6-v2`)

---

## ⚙️ Installation

**1. Clone the Repository**
```bash
git clone [https://github.com/YOUR_USERNAME/DocuChat_AI.git](https://github.com/YOUR_USERNAME/DocuChat_AI.git)
cd DocuChat_AI