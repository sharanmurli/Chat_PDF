

import streamlit as st
from PyPDF2 import PdfReader
import os

from langchain_chroma import Chroma 
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from langchain.schema import Document  
from dotenv import load_dotenv

load_dotenv()

persist_directory = "chroma_db"
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vector_store = Chroma(
    collection_name="pdf_collection",
    embedding_function=embeddings,
    persist_directory=persist_directory
)


def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text: 
                text += page_text
    return text


def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

def store_embeddings_in_chromadb(text_chunks):
    documents = [Document(page_content=chunk, metadata={"source": "uploaded_pdf"}) for chunk in text_chunks]
    vector_store.add_documents(documents)

def display_stored_documents():
    st.subheader("Stored Documents in ChromaDB")
    results = vector_store._collection.get()  
    documents = results.get("documents", [])
    for idx, doc in enumerate(documents):
        preview = doc[:200] + "..." if len(doc) > 200 else doc
        st.write(f"Document {idx + 1} Preview: {preview}")
        st.write("---")

def get_conversational_chain():
    prompt_template = """
    Give me a detailed answer from the provided context and make sure to provide all the necessary details.
    Read the question and understand it carefully and search the documents to find the correct context.
    If the answer is not in the provided context, just say, "answer is not available in the context", don't provide the wrong answer.

    Context:\n {context}\n
    Question:\n {question}\n

    Answer:
    """
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

def user_input(user_question):
    docs = vector_store.similarity_search(user_question, k=3)
    chain = get_conversational_chain()
    response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)
    st.write("Reply: ", response["output_text"])

def delete_collection():
    vector_store._client.delete_collection(name="pdf_collection")
    st.success("Collection 'pdf_collection' has been deleted from ChromaDB.")

def main():
    st.set_page_config(page_title="Chat with PDF using Gemini and ChromaDB")
    st.header("Chat with multiple PDF with Gemini Pro , Langchain and ChromaDB")
    user_question = st.text_input("Ask a question from the PDF Files")
    
    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF Files", accept_multiple_files=True, type=["pdf"])
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                store_embeddings_in_chromadb(text_chunks)
                st.success("Documents processed and stored in ChromaDB!")

        if st.button("View Stored Documents"):
            display_stored_documents()

        if st.button("Delete Collection"):
            delete_collection()

    if user_question:
        user_input(user_question)


if __name__ == "__main__":
    main()

