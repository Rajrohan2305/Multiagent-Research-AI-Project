#load necessary libraries
from dotenv import load_dotenv
load_dotenv()
from langchain_mistralai import ChatMistralAI
from langchain.tools import tool
from tavily import TavilyClient
import os
import requests
from bs4 import BeautifulSoup
from rich import print

# load api key
tavily=TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

# creating our tools
@tool
def web_search(query : str) -> str:
    """search the web for recent and reliable information on a topic .return Title ,url and snippets."""
    results=tavily.search(query=query,max_results=5)
    out=[]
    
    for r in results["results"]:
        out.append(
            f"Title:{r["title"]}\n"
            f"URL : {r["url"]}\n"
            f"Snippet : {r["content"][:300]}"
            )
    return"\n--------\n".join(out)
print(web_search.invoke("what are the recent news of war"))
        
        
@tool
def scrape_url(url : str) -> str:
    """Scrape and return clean text content from the given url for deeper reading"""
    try:
        resp=requests.get(url,timeout=8,headers={"User-Agent":"Mozilla/5.0"})
        soup=BeautifulSoup(resp.text,"html.parser")
        for tag in soup(["script","style","nav","footer"]):
            tag.decomposed()
            return soup.get(separator=" ",strip=True)[:3000]
    except Exception as e:
        return f"could not scrape url:{str(e)}"
    
 