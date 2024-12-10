import networkx as nx

# Simple undirected graph
simple_graph = nx.Graph()
simple_graph.add_edges_from(
    [
        ("A", "B"),
        ("A", "C"),
        ("B", "D"),
        ("B", "E"),
        ("C", "F"),
        ("D", "G"),
        ("E", "H"),
        ("F", "I"),
        ("I", "J"),
        ("I", "B"),
        ("E", "L"),
    ]
)


# Binary tree with integer nodes
binary_tree = nx.balanced_tree(2, 3)

# Graph with weighted edges (for Dijkstra's algorithm), duplicate simple_graph
# with random edge weights
weighted_graph = nx.Graph()
weighted_graph.add_weighted_edges_from(
    [
        ("A", "B", 1),
        ("A", "C", 2),
        ("B", "D", 3),
        ("B", "E", 4),
        ("C", "F", 5),
        ("D", "G", 6),
        ("E", "H", 7),
        ("F", "I", 8),
        ("I", "J", 9),
        ("I", "B", 10),
        ("E", "L", 11),
    ]
)
