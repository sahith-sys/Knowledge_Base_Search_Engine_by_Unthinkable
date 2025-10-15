from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_qa_chain():
    prompt_template = """Answer the question based only on the provided context.
    If not found, say 'Answer not found in the context.'
    
    Context:
    {context}

    Question:
    {question}

    Answer (in 3-4 sentences):
    """

    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2, max_output_tokens=1024, top_p=0.95, top_k=50)
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain
