# --- 4. TRANSFORM QUERY NODE ---
def transform_query(state: AgentState) -> dict:
    print("--- NODE: REWRITING QUERY FOR BETTER RETRIEVAL ---")
    question = state["question"]
    
    prompt = ChatPromptTemplate.from_template(
        """You are a query re-writer optimizing user input for search engine retrieval.
        Look at the input and reason about its underlying intent.
        
        Original Question: {question}
        
        Formulate an improved search query:"""
    )
    
    chain = prompt | llm
    better_query = chain.invoke({"question": question})
    return {"question": better_query.content}

# --- 5. WEB SEARCH NODE (FALLBACK) ---
def web_search(state: AgentState) -> dict:
    print("--- NODE: EXECUTING WEB SEARCH FALLBACK ---")
    question = state["question"]
    documents = state.get("documents", [])
    
    # Simple fallback placeholder (will integrate Tavily API next)
    search_results = f"[Web Search Result]: Additional context retrieved for query '{question}'."
    documents.append(search_results)
    
    return {"documents": documents}