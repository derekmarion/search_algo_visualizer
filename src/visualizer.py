import networkx as nx
import matplotlib.pyplot as plt
from typing import List, Optional


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
        self, start_node: str, goal_node: Optional[str] = None, order: str = "pre"
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
            # Pre-order visit
            if order == "pre":
                if node not in visited:
                    self.visited_order.append(node)
                    visited.add(node)

            # Explore neighbors
            for neighbor in self.graph.neighbors(node):
                if neighbor not in visited:
                    # In-order visit (only for binary trees)
                    if order == "in" and len(list(self.graph.neighbors(node))) > 0:
                        mid_neighbor = list(self.graph.neighbors(node))[0]
                        if mid_neighbor not in visited:
                            dfs_recursive(mid_neighbor)
                            self.visited_order.append(node)

                    dfs_recursive(neighbor)

            # Post-order visit
            if order == "post" and node not in visited:
                self.visited_order.append(node)
                visited.add(node)

        # Start the recursive DFS
        dfs_recursive(start_node)
        return self.visited_order

    def visualize_graph_and_search(
        self,
        search_type: str,
        start_node: str,
        goal_node: Optional[str] = None,
        order: str = "pre",
    ):
        """
        Visualize the graph and search results

        :param search_type: 'bfs' or 'dfs'
        :param start_node: Node to start the search from
        :param goal_node: Optional goal node
        :param order: DFS order ('pre', 'post', 'in')
        """
        # Perform the search
        if search_type == "bfs":
            self.breadth_first_search(start_node, goal_node)
        else:
            self.depth_first_search(start_node, goal_node, order)

        # Visualization
        plt.figure(figsize=(14, 9))
        pos = nx.spring_layout(self.graph, seed=42)

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

        # Create detailed annotation
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
            xy=(0.05, 0.95),  # Position of the annotation
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