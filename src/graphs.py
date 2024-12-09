import networkx as nx

# Simple graph
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
    ]
)

# Binary tree graph
binary_tree = nx.Graph()
binary_tree.add_edges_from(
    [
        ("A", "B"),
        ("A", "C"),
        ("B", "D"),
        ("B", "E"),
        ("C", "F"),
        ("C", "G"),
    ]
)