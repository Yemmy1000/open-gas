from langchain.schema.runnable import RunnableMap, RunnablePassthrough, RunnableLambda
from langchain.schema.output_parser import StrOutputParser
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI

# from embedding.rag_embedding import EmbeddingGeneration
llm = OpenAI()  # Initialize your LLM


import configparser

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the config file
config.read('config')  # Assuming the file is named 'config'

# # Fetch the variables
# GEN_AI = config['DEFAULT']['GEN_AI'].strip('"')
# DOCUMENT_PATH = config['DEFAULT']['DOCUMENT_PATH'].strip('"')
EMBEDDING_PATH = config['DEFAULT']['EMBEDDING_PATH'].strip('"')



# Define a prompt template
prompt_template = PromptTemplate(
    template="Context: {context}\n\nQuestion: {question}\n\nAnswer:",
    input_variables=["context", "question"]
)

class RAG_MODULE:
    def __init__(self):
        self.retriever_instance = EmbeddingRetrieval(EMBEDDING_PATH)

    def get_relevant_context():
        retriever = RunnableLambda(lambda query: self.retriever_instance.retrieve_context(query["question"]))
        return retriever



class rag_chain:
    def __init__(self, prompt):
        self.prompt = prompt
        self.rag_module = RAG_MODULE()
        self.retriver = self.rag_module.get_relevant_context()
    
    
    # Define the RAG chain
    def rag(self):
        rag_chain = (
        RunnableMap({
            "context": self.retriver,  # Use the retriever to fetch context
            "question": RunnablePassthrough()  # Pass the user's question through
        })
        | prompt_template  # Format the prompt with context and question
        | llm  # Generate the answer using the language model
        | StrOutputParser()  # Parse the output to a string
    )
    
        # Example usage
        # result = rag_chain.invoke({self.prompt})
        # print(result)











