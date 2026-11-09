from search_engine import semantic_search

while True:
    query = input(
        "\nWhat service are you looking for? "
        "(Type 'quit' to exit): "
    ).strip()

    if query.lower() == "quit":
        print("Goodbye!")
        break

    results = semantic_search(query, top_k=3)

    if results:
        print("\nMatching services:")

        for number, result in enumerate(results, start=1):
            print(f"\n{number}. {result['document']}")
            print(
                f"   Similarity score: {result['score']:.4f}"
            )
    else:
        print("\nSorry, no relevant services were found.")
