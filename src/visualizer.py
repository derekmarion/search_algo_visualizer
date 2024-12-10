import networkx as nx
import matplotlib.pyplot as plt
from typing import List, Optional, Dict


class GraphSearchAlgorithms:
    def __init__(self, graph: nx.Graph):
        """
        Initialize the graph search algorithms class

        :param graph: NetworkX graph to perform searches on
        """
        self.graph = graph
        self.visited_order = []
        self.search_details = {}

    def breadth_first_search(
        self, start_node: str, goal_node: Optional[str] = None
    ) -> List[str]:
        """
        Perform Breadth-First Search

        :param start_node: Node to start the search from
        :param goal_node: Optional goal node to terminate search
        :return: List of nodes in order of visit
        """
        # Reset visited order and search details
        self.visited_order = []
        self.search_details = {
            "type": "Breadth-First Search (BFS)",
            "start_node": start_node,
            "goal_node": goal_node if goal_node else "Not specified",
        }

        visited = set()
        queue = [start_node]
        visited.add(start_node)

        while queue:
            current_node = queue.pop(0)
            self.visited_order.append(current_node)

            # Goal check
            if current_node == goal_node:
                break

            # Explore unvisited neighbors
            for neighbor in self.graph.neighbors(current_node):
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

        return self.visited_order

    def depth_first_search(
        self, start_node: int, goal_node: Optional[str] = None, order: str = "pre"
    ) -> List[str]:
        """
        Perform Depth-First Search

        :param start_node: Node to start the search from
        :param goal_node: Optional goal node to terminate search
        :param order: 'pre' for pre-order, 'post' for post-order, 'in' for in-order
        :return: List of nodes in order of visit
        """
        # Reset visited order and search details
        self.visited_order = []
        self.search_details = {
            "type": f"Depth-First Search (DFS) - {order.capitalize()}-order",
            "start_node": start_node,
            "goal_node": goal_node if goal_node else "Not specified",
        }

        visited = set()

        def dfs_recursive(node):
            # Prevent revisiting
            if node in visited:
                return

            # Mark as visited immediately to prevent recursion loops
            visited.add(node)

            # Goal check
            if node == goal_node:
                self.visited_order.append(node)
                return

            # Get unvisited neighbors
            unvisited_neighbors = [
                n for n in self.graph.neighbors(node) if n not in visited
            ]

            if order == "pre":
                # Pre-order: Root, Left, Right
                self.visited_order.append(node)

                for neighbor in unvisited_neighbors:
                    dfs_recursive(neighbor)

            elif order == "in":
                # In-order: Left, Root, Right
                # Sort neighbors to ensure consistent left-right traversal
                unvisited_neighbors.sort()
                
                if unvisited_neighbors:
                    # Left subtree first
                    left_child = unvisited_neighbors[0]
                    if left_child: 
                        dfs_recursive(left_child)

                # Current node
                self.visited_order.append(node)

                if unvisited_neighbors:
                    # Right subtree
                    right_child = unvisited_neighbors[1]
                    if right_child:
                        dfs_recursive(right_child)

            elif order == "post":
                # Post-order: Left, Right, Root
                for neighbor in unvisited_neighbors:
                    dfs_recursive(neighbor)

                self.visited_order.append(node)

        # Start the recursive DFS
        dfs_recursive(start_node)
        return self.visited_order

    def dijkstra(self, start_node: str, goal_node: Optional[str] = None) -> List[str]:
        """
        Perform Dijkstra's algorithm

        :param start_node: Node to start the search from
        :param goal_node: Optional goal node to terminate search
        :return: List of nodes in order of visit
        """
        # Reset visited order and search details
        self.visited_order = []
        self.search_details = {
            "type": "Dijkstra's Algorithm",
            "start_node": start_node,
            "goal_node": goal_node if goal_node else "Not specified",
        }

        # Initialize distances and visited set
        distances = {node: float("inf") for node in self.graph.nodes}
        distances[start_node] = 0
        visited = set()

        while len(visited) < len(self.graph.nodes):
            # Set current node to unvisited node with smallest distance
            current_node = min(
                (node for node in self.graph.nodes if node not in visited),
                key=lambda node: distances[node],
            )
            visited.add(current_node)
            self.visited_order.append(current_node)

            # End search if goal node is reached
            if current_node == goal_node:
                break

            # Check neighbors of current node for shorter paths and update distances
            for neighbor, weight in self.graph[current_node].items():
                if neighbor not in visited:
                    new_distance = distances[current_node] + weight["weight"]
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance

        return self.visited_order

    def create_pyramidal_layout(self) -> Dict:
        """
        Create a pyramidal layout for a balanced binary tree

        :return: Dictionary of node positions
        """

        def get_tree_height(graph):
            """Calculate the height of the tree"""
            return max(
                len(nx.shortest_path(graph, 0, leaf))
                for leaf in graph.nodes
                if graph.degree(leaf) == 1
            )

        height = get_tree_height(self.graph)
        pos = {}

        # Process nodes level by level
        for level in range(height + 1):
            # Find nodes at this level
            level_nodes = [
                node
                for node in self.graph.nodes()
                if len(nx.shortest_path(self.graph, 0, node)) - 1 == level
            ]

            # Calculate width of this level
            level_width = len(level_nodes)

            # Position nodes horizontally
            for i, node in enumerate(sorted(level_nodes)):
                x = (i - (level_width - 1) / 2) / (level_width / 2)
                y = 1 - (level / height)
                pos[node] = (x, y)

        return pos

    def visualize_graph_and_search(
        self,
        search_type: str,
        start_node: str,
        goal_node: Optional[str] = None,
        order: str = "pre",
    ):
        """
        Visualize the graph and search results

        :param search_type: 'bfs', 'dfs' or 'dijkstra'
        :param start_node: Node to start the search from
        :param goal_node: Optional goal node
        :param order: DFS order ('pre', 'post', 'in')
        """
        # Perform the search
        if search_type == "bfs":
            self.breadth_first_search(start_node, goal_node)
        elif search_type == "dijkstra":
            self.dijkstra(start_node, goal_node)
        else:
            self.depth_first_search(start_node, goal_node, order)

        # If input graph has integer nodes, convert
        # visited order to strings to enable visualization
        if all(isinstance(node, int) for node in self.graph.nodes):
            self.visited_order = [str(node) for node in self.visited_order]

        # Print visited order for debugging
        print("Visited Order:", " → ".join(self.visited_order))

        # Set plot size
        plt.figure(figsize=(14, 9))
        pos = None

        # Conditional layout based on graph type
        if search_type == "bfs" or search_type == "dijkstra":
            pos = nx.spring_layout(self.graph, seed=13)
            # Add edge weights to graph if available
            edge_labels = nx.get_edge_attributes(self.graph, "weight")
            nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)
        elif search_type == "dfs":
            pos = self.create_pyramidal_layout()

        # Draw the graph
        nx.draw(
            self.graph,
            pos,
            with_labels=True,
            node_color="lightblue",
            node_size=500,
            font_size=10,
            font_weight="bold",
        )

        # Create detailed annotation for
        annotation_text = (
            f"Search Details:\n"
            f"Algorithm: {self.search_details['type']}\n"
            f"Start Node: {self.search_details['start_node']}\n"
            f"Target Node: {self.search_details['goal_node']}\n\n"
            f"Visited Order:\n{' → '.join(self.visited_order)}"
        )

        # Add annotation to the plot
        plt.annotate(
            annotation_text,
            xy=(0.05, 0.90),  # Position of the annotation
            xycoords="axes fraction",
            fontsize=9,
            bbox=dict(boxstyle="round,pad=0.5", fc="yellow", alpha=0.5),
            verticalalignment="top",
        )

        # Set title
        plt.title("Graph Search Visualization")

        # Show the plot
        plt.tight_layout()
        plt.show()
