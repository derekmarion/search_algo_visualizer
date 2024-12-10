import networkx as nx
import math

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


# Create a sequential binary search tree of 15 nodes
binary_search_tree = nx.Graph()
binary_search_tree.add_edges_from(
    [
        (8, 4),
        (8, 12),
        (4, 2),
        (4, 6),
        (12, 10),
        (12, 14),
        (2, 1),
        (2, 3),
        (6, 5),
        (6, 7),
        (10, 9),
        (10, 11),
        (14, 13),
        (14, 15),
    ]
)


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

# Graph with weighted edges and arbitrary heuristics (for A* algorithm)
# TODO: Add more nodes and edges to this graph to demonstrate the A* algorithm
weighted_graph_with_heuristics = nx.Graph()
weighted_graph_with_heuristics.add_weighted_edges_from(
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

# Define coordinates for each node to calculate the heuristic
node_positions = {
    "A": (0, 0),
    "B": (1, 2),
    "C": (2, 1),
    "D": (3, 3),
    "E": (4, 2),
    "F": (5, 1),
    "G": (6, 3),
    "H": (7, 2),
    "I": (8, 1),
    "J": (9, 3),
    "L": (10, 2),
}


# Function to calculate Euclidean distance
def euclidean_distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)


# Add heuristic (straight-line distance from node "A") to each node
heuristics = {}
for node in weighted_graph_with_heuristics.nodes:
    heuristics[node] = euclidean_distance(node_positions["A"], node_positions[node])

# Add heuristics as node attributes
nx.set_node_attributes(weighted_graph_with_heuristics, heuristics, "heuristic")
