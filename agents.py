from langchain.agents import create_agent
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search,scrape_url
from dotenv import load_dotenv
load_dotenv()


# model
llm=ChatMistralAI(model="mistral-small-2506",temperature=0)


#1st agent

def build_search_agent():
    return create_agent(
        model=llm,
        tools=[web_search]
    )
    
    
# 2nd agent

def build_reader_agent():
    return create_agent(
        model=llm,
        tools=[scrape_url]
    )
    


# writer chain(agent)

writer_prompt=ChatPromptTemplate.from_messages([
("system","you are an expert research writter. write clear ,structured and insightful report."),
("human","""write a detailed research report on the given topic below.
Topic:{topic}
research gathered:{research}
                                                
Structure the report as:
-Introduction
-Key Findings(minimum 3 well-explained points)
-Conclusion
-Sources(list all urls found in the research)
                                                
be detailed,factual and professional."""),
])

writer_chain=writer_prompt | llm | StrOutputParser()


#critic_chain

critic_prompt=ChatPromptTemplate.from_messages([
    ("system","you are a sharp and constructive research critic.be honest and specific."),
    ("human","""review the research report  below and evaluate it strictly.
     Report:{report}
     
     Respond in the exact format:
    Score:X/10
    
    Strengths:
    -.....
    -.....
    
    Areas to Improve:
    -....
    -....
    
    
    one line Verdict:
    ......""")
])


critic_chain=critic_prompt | llm | StrOutputParser()