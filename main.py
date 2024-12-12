from src import GraphSearchAlgorithms
from src import (
    simple_graph,
    weighted_graph,
    binary_search_tree,
    weighted_graph_with_heuristics,
)


def main():
    # Depth-First Search (DFS) with pre-order, in-order, and post-order
    search = GraphSearchAlgorithms(binary_search_tree)
    search.visualize_graph_and_search("dfs", start_node=8, order="pre")
    search.visualize_graph_and_search("dfs", start_node=8, order="in")
    search.visualize_graph_and_search("dfs", start_node=8, order="post")

    # Breadth-First Search (BFS)
    search = GraphSearchAlgorithms(simple_graph)
    search.visualize_graph_and_search("bfs", start_node="A", goal_node="L")

    # Dijkstra's algorithm with target node
    search = GraphSearchAlgorithms(weighted_graph)
    search.visualize_graph_and_search("dijkstra", start_node="A", goal_node="F")

    # A* algorithm with target node
    search = GraphSearchAlgorithms(weighted_graph_with_heuristics)
    search.visualize_graph_and_search("astar", start_node="A", goal_node="F")


if __name__ == "__main__":
    main()
