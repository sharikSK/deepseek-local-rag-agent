from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.tools import ExaTools

def get_web_search_agent() -> Agent:
    return Agent(
        name="Web Search Agent",
        model=Ollama(id="llama3.2"),
        tools=[ExaTools(
            api_key="your_exa_api_key",
            include_domains=["example.com"],
            num_results=5
        )],
        instructions="""You are a web search expert...""",
        show_tool_calls=True,
        markdown=True,
    )

def get_rag_agent() -> Agent:
    return Agent(
        name="DeepSeek RAG Agent",
        model=Ollama(id="deepseek-r1:1.5b"),
        instructions="""You are an Intelligent Agent...""",
        show_tool_calls=True,
        markdown=True,
    )
