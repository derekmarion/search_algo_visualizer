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

# Binary tree with numbers as nodes
binary_tree = nx.Graph()
binary_tree.add_edges_from(
    [
        (1, 2),
        (1, 3),
        (2, 4),
        (2, 5),
        (3, 6),
        (3, 7),
        (4, 8),
        (4, 9),
        (5, 10),
        (5, 11),
        (6, 12),
        (6, 13),
    ]
)

# Graph with weighted edges (for Dijkstra's algorithm)
weighted_graph = nx.Graph()
weighted_graph.add_weighted_edges_from(
    [
        ("A", "B", 1),
        ("A", "C", 3),
        ("B", "D", 2),
        ("B", "E", 4),
        ("C", "F", 5),
        ("D", "G", 6),
        ("E", "H", 7),
        ("F", "I", 8),
    ]
)