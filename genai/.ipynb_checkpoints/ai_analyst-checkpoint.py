import openai
# from openai import OpenAI
import time
import random


import os
from openai import OpenAI
import configparser
from rag.rag_embedding_retriever import EmbeddingRetrieval
# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the config file
config.read('config')  # Assuming the file is named 'config'

# Fetch the variables
GEN_AI = config['DEFAULT']['GEN_AI'].strip('"')
# DOCUMENT_PATH = config['DEFAULT']['DOCUMENT_PATH'].strip('"')
EMBEDDING_PATH = config['DEFAULT']['EMBEDDING_PATH'].strip('"')




class AI_Analyst:
    def __init__(self):
        self.model= GEN_AI

    def get_rag(self, prompt):
        # Initialize retriever
        retriever_instance = EmbeddingRetrieval(EMBEDDING_PATH)
        return retriever_instance.retrieve_context(prompt)
        
        
    def get_completion(self, prompt):

        # openai.api_key = get_openai_key
        # messages = prompts
        client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
            # api_key = get_openai_key
        ) 
        # print("Context", self.get_rag(prompt))
        messages = [
            {
                "role": "system", 
                "content":"You are a cybersecurity and information security expert. \
                    Note: only produce the quality, professional and verifiable contents"
            },
            {
                "role": "user", 
                "content": f"{prompt} \n \n context: {self.get_rag(prompt)}"
            },
        ]


        chat_completion = client.chat.completions.create(
            messages=messages,
            model=self.model,
        )
       
        return chat_completion.choices[0].message.content 


    def analyse(self, prompts):
        while True:
            try:
                #print(question)
                result = self.get_completion(prompts)
                #print(result,'\n')
                # predictions.append(result)
                #print(predictions, resp_word_len)
                break
            except openai.APIConnectionError as e:
                print("The server could not be reached")
                print(e.__cause__)  # an underlying Exception, likely raised within httpx.
            except openai.RateLimitError as e:
                print("A 429 status code was received; we should back off a bit.")
            except openai.APIStatusError as e:
                print("Another non-200-range status code was received")
                print(e.status_code)
                print(e.response)
    
        return result
    

def main():
    analyst = AI_Analyst()
    input_ = input(": > ")
    response = analyst.analyse(input_)
    print("\n\nResponse: ")
    print(response)

# Entry point of the script
if __name__ == "__main__":    
    from rich.console import Console
    from rich.markdown import Markdown
    # draw_cube()
    main()