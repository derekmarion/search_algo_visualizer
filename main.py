from src import GraphSearchAlgorithms
from src import simple_graph


def main():
    # Initialize the search algorithms
    search = GraphSearchAlgorithms(simple_graph)

    # Demonstrate different search types
    print("Breadth-First Search:")
    search.visualize_graph_and_search("bfs", start_node="A")


if __name__ == "__main__":
    main()
