from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser


information = """
Elon Reeve Musk FRS (/ˈiːlɒn/ EE-lon; born June 28, 1971) is a businessman. He is known for his leadership of Tesla, SpaceX, X (formerly Twitter), and the Department of Government Efficiency (DOGE). Musk has been considered the wealthiest person in the world since 2021; as of May 2025, Forbes estimates his net worth to be US$424.7 billion.

Born to a wealthy family in Pretoria, South Africa, Musk emigrated in 1989 to Canada. He received bachelor's degrees from the University of Pennsylvania in 1997 before moving to California, United States, to pursue business ventures. In 1995, Musk co-founded the software company Zip2. Following its sale in 1999, he co-founded X.com, an online payment company that later merged to form PayPal, which was acquired by eBay in 2002. That year, Musk also became an American citizen.
"""

if __name__ == "__main__":
    load_dotenv()
    print("Hello Langchain")
    print(os.environ['COOL_API_KEY'])

    summary_template = """
            given the information {information} about a person from I want you to create
            1. a short summary
            2. two interesting facts about them
    """

    summary_promt_template = PromptTemplate(input_variables="information", template=summary_template)

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    llm2 = ChatOllama(model="llama3")
    chain = summary_promt_template | llm

    res = chain.invoke(input={"information": information})

    print(res)

    chain2 = summary_promt_template | llm2 | StrOutputParser()
    res = chain2.invoke(input={"information": information})
    print(res)
