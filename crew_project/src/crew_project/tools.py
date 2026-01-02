import os 
from exa_py import Exa
from langchain.agents import Tool

class ExaSearchtoolSet():
    @Tool
    def search(query: str):
        """Searching the webpage based on a query."""
        return ExaSearchtoolSet._exa().search(f"{query}", num_results=3, use_autoprompt=True)

    @Tool
    def find_similar(url: str):
        """Finding similar content based on the provided url.
            the url passed in should be returned from the search tool."""
        return ExaSearchtoolSet._exa().find_similar(url, num_results=3)
    
    @Tool
    def get_contents(ids: str):
      """Get the contents of a webpage.
      The ids must be passed in as a list, a list of ids returned from `search`.
      """
      ids = eval(ids)

      contents = str(ExaSearchtoolSet._exa().get_contents(ids))
      contents = contents.split("URL:")
      contents = [content[:1000] for content in contents]
      return "\n\n".join(contents)
    

    def tools():
        return [
        ExaSearchtoolSet.search,
        ExaSearchtoolSet.find_similar,
        ExaSearchtoolSet.get_contents
    ]

    def _exa():
        return Exa(api_key=os.getenv("EXA_API_KEY"))