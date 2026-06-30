# src/tools.py
from langchain_community.tools.tavily_search import TavilySearchResults

def get_search_tool():
    return TavilySearchResults(
        max_results=3,
        search_depth="advanced",
        tavily_api_key="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" # Clé en dur
    )