from langgraph.graph import END, StateGraph

from src.core.edges import decide_to_generate
from src.core.nodes import generate, grade_documents, retrieve, transform_query, web_search
from src.core.state import AgentState

def build_crag_graph():
    workflow = StateGraph(AgentState)

    # 1. Add Nodes
    workflow.add_node("retrieve", retrieve)
    workflow.add_node("grade_documents", grade_documents)
    workflow.add_node("generate", generate)
    workflow.add_node("transform_query", transform_query)
    workflow.add_node("web_search", web_search)

    # 2. Set Entry Point
    workflow.set_entry_point("retrieve")

    # 3. Add Edges
    workflow.add_edge("retrieve", "grade_documents")
    
    # Conditional edge after grading
    workflow.add_conditional_edges(
        "grade_documents",
        decide_to_generate,
        {
            "transform_query": "transform_query",
            "generate": "generate",
        },
    )
    
    # Fallback path loops back to generation
    workflow.add_edge("transform_query", "web_search")
    workflow.add_edge("web_search", "generate")
    workflow.add_edge("generate", END)

    return workflow.compile()

# Instantiated executable graph
app = build_crag_graph()