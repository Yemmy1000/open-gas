import os
from dotenv import load_dotenv
import logging
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

# Load environment variables
load_dotenv()
embeddings = OpenAIEmbeddings()


import configparser

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the config file
config.read('config')  # Assuming the file is named 'config'

# # Fetch the variables
# embedded_path = config['DEFAULT']['EMBEDDING_PATH'].strip('"')


class EmbeddingRetrieval:
    def __init__(self, embeddingpath):
        self.vectorstore = FAISS.load_local(
            embeddingpath, embeddings, allow_dangerous_deserialization=True
        )

    def retrieve_context(self, query, k=5):
        """Retrieve and print relevant contexts based on similarity search."""
        results = self.vectorstore.similarity_search(query, k=k)  # Fetch top-k matches
        context = "\n".join([doc.page_content for doc in results]) if results else "No relevant context found."
        # print("\n======================= Retrieved Context =======================\n", context, "\n======================= Retrieved Context =======================\n")  # Print the relevant context
        return context

if __name__ == "__main__":
    from langchain_openai import OpenAIEmbeddings
    load_dotenv()
    embeddings = OpenAIEmbeddings()


    # Initialize embeddings
    embeddings = OpenAIEmbeddings()

    # Specify the folder containing PDF files
    # folder_path = "../document/pdf_doc"

    # Create an instance of EmbeddingGeneration
    embedding_retr = EmbeddingRetrieval("../embedded_doc/doc_faiss_index")  # Path to the FAISS index

    # Generate embeddings
    rt = embedding_retr.retrieve_context("During Night Dragon techniques, attacker exploit public-facing application threat actors used SQL injection exploits against extranet web servers to gain access.")








