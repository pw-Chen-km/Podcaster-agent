from langchain_community.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os


def setup_llm_chain():
    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature=0.7,
        api_key=os.environ["OPENAI_API_KEY"]
    )
    
    prompt = PromptTemplate(
        input_variables=["episode_number", "context", "question"],
        template="""根據第 {episode_number} 集的內容回答問題。

相關內容：{context}

問題：{question}

請以「根據第 {episode_number} 集的內容」開始回答。"""
    )
    
    llm_chain = LLMChain(llm=llm, prompt=prompt)
    return llm_chain

def generate_stylized_response(question, episode_data):
    llm_chain = setup_llm_chain()
    response = llm_chain.invoke({
        "episode_number": episode_data['episode_number'],
        "context": episode_data['transcript'],
        "question": question
    })
    return response["text"]

def setup_llm_chain():
    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature=0.2,
        api_key=os.environ["OPENAI_API_KEY"]
    )
    
    prompt = PromptTemplate(
        input_variables=["episode_number", "context", "question"],
        template="""根據第 {episode_number} 集的內容回答問題。

相關內容：{context}

問題：{question}

請以「根據第 {episode_number} 集的內容」開始回答。"""
    )
    
    llm_chain = LLMChain(llm=llm, prompt=prompt)
    return llm_chain

def generate_stylized_response(question, episode_data):
    llm_chain = setup_llm_chain()
    response = llm_chain.invoke({
        "episode_number": episode_data['episode_number'],
        "context": episode_data['transcript'],
        "question": question
    })
    return response["text"] 