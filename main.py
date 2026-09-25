from src.core.graph import app

def run_test():
    # Test Query 1: Relevant to sample data (should go directly to generate)
    query_1 = "What is Corrective RAG?"
    print(f"\n==================== TEST 1 ====================")
    inputs = {"question": query_1, "retry_count": 0}
    result_1 = app.invoke(inputs)
    print(f"\n[FINAL RESPONSE 1]:\n{result_1['generation']}")

    # Test Query 2: Irrelevant to local sample data (should trigger transform_query & web_search)
    query_2 = "Who won the World Cup in 2022?"
    print(f"\n==================== TEST 2 ====================")
    inputs_2 = {"question": query_2, "retry_count": 0}
    result_2 = app.invoke(inputs_2)
    print(f"\n[FINAL RESPONSE 2]:\n{result_2['generation']}")

if __name__ == "__main__":
    run_test()