Here's a detailed and engaging GitHub README for your project:

---

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

## 🛑 Prerequisites
Make sure you have the following installed:
- **Python 3.7+**
- **pip** for installing dependencies
- **Streamlit** for the frontend

---

## 🏗️ Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/chat-with-multiple-pdfs.git
   cd chat-with-multiple-pdfs
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**
   - Create a `.env` file in the root directory and add your API keys and other sensitive information:
     ```
     GOOGLE_API_KEY=your_google_api_key
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

## 🖥️ User Interface
- **Streamlit Sidebar**: 
  - **Upload PDFs**: Upload multiple PDF files.
  - **Submit & Process**: Process and store the PDFs in ChromaDB.
  - **View Stored Documents**: Preview the first few lines of stored documents.
  - **Delete Collection**: Delete all stored documents from ChromaDB.
- **Main Area**: Ask questions and view the responses.

---

## 📦 Technologies Used
- **Gemini Pro** 🤖: Advanced generative AI model for question answering.
- **Langchain** 🧩: Framework for building language model applications.
- **FAISS** 🗃️: Library for efficient similarity search and clustering.
- **ChromaDB** 🏗️: Open-source database for embedding storage.
- **Streamlit** 🌐: Framework for creating interactive web apps with Python.

---

## 📝 Future Improvements
- **🔍 Enhanced Search**: Integrate more sophisticated search and ranking algorithms.
- **🖼️ File Support**: Extend support to other file formats like Word documents.
- **🌐 Deploy**: Deploy the app on a cloud service for public access.

---

## 🛡️ Security
- **.env File**: Make sure your `.env` file is listed in `.gitignore` to prevent sensitive information from being pushed to GitHub.
- **API Keys**: Keep your API keys secure and use environment variables to manage them.

---

## 🤝 Contributing
Contributions are welcome! Feel free to open issues or submit pull requests for improvements or bug fixes.

---

## 📄 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

## 🌟 Acknowledgments
- Thanks to **Langchain** and **OpenAI** for making powerful tools accessible!
- Inspired by the need to create more interactive and intelligent document-based search systems.

---

## 📞 Contact
For questions or feedback, please reach out to [your email] or create an issue in the repository.

---

Feel free to personalize this README and add your own GitHub repository link, contact information, and future plans. Let me know if you need any changes or have any other requirements!
