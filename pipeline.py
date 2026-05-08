from agents import build_search_agent, build_reader_agent, writer_chain, critic_chain
from rich import print


def run_research_pipeline(topic: str) -> dict:

    state = {}

    # search agent working
    print("step-1 search agent working")

    search_agent = build_search_agent()

    search_result = search_agent.invoke({
        "messages": [
            ("user", f"Find Recent,reliable and detailed information about:{topic}")
        ]
    })

    state["search_results"] = search_result["messages"][-1].content

    print("\n search_results", state["search_results"])

    # step-2 reader agent

    print("\n step-2 reader agent is scraping top resources....")

    reader_agent = build_reader_agent()

    reader_result = reader_agent.invoke({
        "messages": [
            ("user",
             f"Based on the following search results about '{topic}', "
             f"pick the most revelent url and scrape it for deeper content.\n\n"
             f"search results : \n {state['search_results'][:800]}")
        ]
    })

    state["scraped_content"] = reader_result["messages"][-1].content

    print("\n scraped_content: \n", state["scraped_content"])

    # step-3 writer chain

    print("step-3 Writer is drafting the report......")

    research_combined = (
        f"SEARCH RESULTS : \n {state['search_results']}\n\n"
        f"DETAILED SCRAPED CONTENT : {state['scraped_content']}"
    )

    state["report"] = writer_chain.invoke({
        "topic": topic,
        "research": research_combined
    })

    print("\n Final Report \n", state["report"])

    # critic report

    print("step-4 critic is reviewing the report")

    state["feedback"] = critic_chain.invoke({
        "report": state["report"]
    })

    print("\n critic report \n", state["feedback"])

    return state


if __name__ == "__main__":

    topic = input("\n Enter a Research topic : ")

    run_research_pipeline(topic)