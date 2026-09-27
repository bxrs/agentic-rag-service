from typing import List, TypedDict

class AgentState(TypedDict):
    """
    Represents the state passed between nodes in the graph.
    
    question: the current user question (may get rewritten)
    documents: list of retrieved document chunks (as strings, for now)
    generation: the final LLM answer
    web_search_needed: "Yes"/"No" flag set by grade_documents
    """
    question: str
    documents: List[str]
    generation: str
    web_search_needed: str