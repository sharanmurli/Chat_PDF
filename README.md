# Chat with Multiple PDFs using Gemini Pro, Langchain, FAISS, ChromaDB, and Streamlit! 📚🤖✨

Welcome to the **Chat with PDF** project! This application allows users to upload multiple PDF documents and ask questions about the content within them. Using **Gemini Pro**, **Langchain**, **FAISS**, and **ChromaDB**, we create an efficient and intelligent system that provides contextual answers based on the uploaded documents, all with a sleek **Streamlit** frontend.

---

## 🛠️ Features
- **📄 Multi-PDF Support**: Upload multiple PDF files and ask questions based on their content.
- **🧠 Advanced Question Answering**: Uses **Langchain** with **Gemini Pro** for natural language understanding and response generation.
- **💾 Local Storage with FAISS**: Efficiently stores and retrieves embeddings for similarity search.
- **🗂️ Persistent Storage with ChromaDB**: Keeps document embeddings across sessions.
- **🎛️ Interactive UI with Streamlit**: User-friendly interface for uploading files, asking questions, and managing the database.

---

## Prerequisites
Make sure you have the following installed:
- **Python 3.9+**
- **pip** for installing dependencies
- **Streamlit** for the frontend

---

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/sharanmurli/Chat_PDF.git
   cd Chat_PDF
   ```

2. **Create a Virtual Environment**
   - **On Windows**:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - **On macOS/Linux**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**
   - Create a `.env` file in the root directory and add your API keys and other sensitive information:
     ```
     GOOGLE_API_KEY="your_google_api_key"
     ```

---

## 🚀 Running the Application

1. **Run the Streamlit App**
   ```bash
   streamlit run app.py
   ```

2. **Upload PDFs**: Use the sidebar to upload your PDF documents.
3. **Ask Questions**: Type your question in the input box and get contextual answers based on the content of the PDFs.
4. **View or Delete Documents**: Manage your uploaded documents using the sidebar options.

---

## 🔧 How It Works
1. **Extract Text**: The text is extracted from uploaded PDF files using `PyPDF2`.
2. **Split Text into Chunks**: The text is split into manageable chunks using **Langchain's RecursiveCharacterTextSplitter**.
3. **Generate Embeddings**: Embeddings are generated using **Google Generative AI Embeddings**.
4. **Store Embeddings**: 
   - **FAISS**: For fast, local similarity search.
   - **ChromaDB**: For persistent storage of embeddings.
5. **Answer Questions**: The **Langchain** framework is used to build a conversational chain that searches for the most relevant chunks and generates a detailed answer.

---

## 📦 Technologies Used
- **Gemini Pro** 🤖: Advanced generative AI model for question answering.
- **Langchain** 🧩: Framework for building language model applications.
- **FAISS** 🗃️: Library for efficient similarity search and clustering.
- **ChromaDB** 🏗️: Open-source database for embedding storage.
- **Streamlit** 🌐: Framework for creating interactive web apps with Python.

---

## 🛡️ Security
- **.env File**: Make sure your `.env` file is listed in `.gitignore` to prevent sensitive information from being pushed to GitHub.
- **API Keys**: Keep your API keys secure and use environment variables to manage them.

---

