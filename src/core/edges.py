from src.core.state import AgentState

def decide_to_generate(state: AgentState) -> str:
    """
    Determines whether to generate an answer or fall back to web search/rewriting.
    """
    print("--- EDGE: DECIDING NEXT STEP ---")
    web_search = state.get("web_search_needed", "No")
    
    if web_search == "Yes":
        # Context was graded irrelevant or low quality
        print("--- DECISION: DOCUMENTS ARE IRRELEVANT -> TRANSFORM QUERY / FALLBACK ---")
        return "transform_query"
    else:
        # Context is relevant
        print("--- DECISION: DOCUMENTS ARE RELEVANT -> GENERATE ANSWER ---")
        return "generate"