from collections import deque
from collections.abc import Hashable, Iterable, Mapping

#  (Node, Neighbour) | (Node, Neighbour, Weight)
type Edge[NodeT] = tuple[NodeT, NodeT] | tuple[NodeT, NodeT, int]

#  node -> [neighbour, ...]
type AdjacencyList[NodeT] = Mapping[NodeT, Iterable[NodeT]]

#  node -> {neighbour: weight, ...}
type WeightedAdjacencyList[NodeT] = Mapping[NodeT, Mapping[NodeT, int]]


class Graph[NodeT: Hashable]:
    """Generic directed graph, geared primarily towards DAG-style puzzles.

    Stores nodes and weighted directed edges in an adjacency mapping.
    Provides traversal, ordering, and cycle-detection helpers commonly
    needed for Advent of Code dependency/graph puzzles (e.g. topological
    sort of prerequisites, longest/shortest path in a DAG).
    """

    def __init__(self) -> None:
        self._adjacency: dict[NodeT, dict[NodeT, int]] = {}

    @classmethod
    def from_edges(cls, edges: Iterable[Edge[NodeT]]) -> "Graph[NodeT]":
        """Build a graph from an iterable of (source, target[, weight]) tuples."""
        graph: Graph[NodeT] = cls()
        for edge in edges:
            match edge:
                case (source, target, weight):
                    graph.add_edge(source, target, weight)
                case (source, target):
                    graph.add_edge(source, target)
        return graph

    @classmethod
    def from_adjacency_list(cls, adjacency: AdjacencyList[NodeT]) -> "Graph[NodeT]":
        """Build a graph from an unweighted adjacency-list mapping.

        Each value is an iterable of neighbors (edge weight defaults to 1).
        Nodes with no neighbors (empty iterable) are still registered.

        Example:
            >>> graph = Graph.from_adjacency_list({"a": ["b", "c"], "b": ["c"], "c": []})
            >>> graph.edges()
            [('a', 'b', 1), ('a', 'c', 1), ('b', 'c', 1)]
        """
        graph: Graph[NodeT] = cls()
        for node, neighbors in adjacency.items():
            graph.add_node(node)
            for neighbor in neighbors:
                graph.add_edge(node, neighbor)
        return graph

    @classmethod
    def from_weighted_adjacency_list(
        cls, adjacency: WeightedAdjacencyList[NodeT]
    ) -> "Graph[NodeT]":
        """Build a graph from a weighted adjacency-list mapping.

        Each value is a mapping of neighbor -> weight. Nodes with no
        neighbors (empty mapping) are still registered.

        Example:
            >>> graph = Graph.from_weighted_adjacency_list({"a": {"b": 2, "c": 5}, "c": {}})
            >>> graph.edges()
            [('a', 'b', 2), ('a', 'c', 5)]
        """
        graph: Graph[NodeT] = cls()
        for node, neighbors in adjacency.items():
            graph.add_node(node)
            for neighbor, weight in neighbors.items():
                graph.add_edge(node, neighbor, weight)
        return graph

    def add_node(self, node: NodeT) -> None:
        """Register a node, even if it has no edges yet."""
        self._adjacency.setdefault(node, {})

    def add_edge(self, source: NodeT, target: NodeT, weight: int = 1) -> None:
        """Add a directed edge from source to target with an optional weight."""
        self.add_node(source)
        self.add_node(target)
        self._adjacency[source][target] = weight

    @property
    def nodes(self) -> set[NodeT]:
        """Return all nodes currently in the graph."""
        return set(self._adjacency)

    def neighbors(self, node: NodeT) -> dict[NodeT, int]:
        """Return the outgoing neighbors of a node mapped to their edge weights."""
        return dict(self._adjacency.get(node, {}))

    def in_degree(self, node: NodeT) -> int:
        """Return the number of incoming edges to a node."""
        return sum(1 for targets in self._adjacency.values() if node in targets)

    def out_degree(self, node: NodeT) -> int:
        """Return the number of outgoing edges from a node."""
        return len(self._adjacency.get(node, {}))

    def direct_dependencies(self, node: NodeT) -> set[NodeT]:
        """Return the direct predecessors of a node (nodes with an edge into it).

        Example:
            >>> graph = Graph.from_edges([("a", "c"), ("b", "c"), ("c", "d")])
            >>> sorted(graph.direct_dependencies("c"))
            ['a', 'b']
        """
        return {source for source, targets in self._adjacency.items() if node in targets}

    def dependencies(self, node: NodeT) -> set[NodeT]:
        """Return every node that must come before ``node`` (transitive predecessors).

        Useful for DAG-style "prerequisite" puzzles: walks backwards through
        all incoming edges, collecting the full set of ancestors.

        Example:
            >>> graph = Graph.from_edges([("a", "b"), ("b", "c"), ("a", "c")])
            >>> sorted(graph.dependencies("c"))
            ['a', 'b']
        """
        visited: set[NodeT] = set()
        queue: deque[NodeT] = deque(self.direct_dependencies(node))

        while queue:
            current = queue.popleft()
            if current in visited:
                continue
            visited.add(current)
            queue.extend(self.direct_dependencies(current) - visited)

        return visited

    def dependency_order(self, node: NodeT) -> list[NodeT]:
        """Return a topological order of every ancestor of ``node``, ending with
        ``node`` itself.

        Walks backwards through predecessors (DFS post-order), so each node
        only appears once its own dependencies have already been listed.
        Raises ValueError if a cycle is detected among the ancestors.

        Example:
            >>> graph = Graph.from_edges([("a", "b"), ("b", "c"), ("a", "c")])
            >>> graph.dependency_order("c")
            ['a', 'b', 'c']
        """
        order: list[NodeT] = []
        visited: set[NodeT] = set()
        in_progress: set[NodeT] = set()

        def visit(current: NodeT) -> None:
            if current in visited:
                return
            if current in in_progress:
                raise ValueError("Graph contains a cycle; dependency order requires a DAG")

            in_progress.add(current)
            for dependency in self.direct_dependencies(current):
                visit(dependency)
            in_progress.remove(current)

            visited.add(current)
            order.append(current)

        visit(node)
        return order

    def edges(self) -> list[tuple[NodeT, NodeT, int]]:
        """Return all edges as (source, target, weight) tuples."""
        return [
            (source, target, weight)
            for source, targets in self._adjacency.items()
            for target, weight in targets.items()
        ]

    def topological_sort(self) -> list[NodeT]:
        """Return nodes in topological order using Kahn's algorithm.

        Raises ValueError if the graph contains a cycle (i.e. is not a DAG).
        """
        in_degree: dict[NodeT, int] = dict.fromkeys(self._adjacency, 0)
        for targets in self._adjacency.values():
            for target in targets:
                in_degree[target] += 1

        queue: deque[NodeT] = deque(node for node, degree in in_degree.items() if degree == 0)
        order: list[NodeT] = []

        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in self._adjacency.get(node, {}):
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(order) != len(self._adjacency):
            raise ValueError("Graph contains a cycle; topological sort requires a DAG")

        return order

    def has_cycle(self) -> bool:
        """Return whether the graph contains a cycle.

        TODO: sheep and wolf algorith, Floyd's."""
        try:
            self.topological_sort()
        except ValueError:
            return True
        return False

    def bfs(self, start: NodeT) -> list[NodeT]:
        """Return nodes reachable from start in breadth-first order."""
        visited: set[NodeT] = {start}
        order: list[NodeT] = [start]
        queue: deque[NodeT] = deque([start])

        while queue:
            node = queue.popleft()
            for neighbor in self._adjacency.get(node, {}):
                if neighbor not in visited:
                    visited.add(neighbor)
                    order.append(neighbor)
                    queue.append(neighbor)

        return order

    def dfs(self, start: NodeT) -> list[NodeT]:
        """Return nodes reachable from start in depth-first (pre-order) order."""
        visited: set[NodeT] = set()
        order: list[NodeT] = []
        stack: list[NodeT] = [start]

        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            order.append(node)

            stack.extend(
                neighbor
                for neighbor in reversed(self._adjacency.get(node, {}))
                if neighbor not in visited
            )

        return order

    def longest_path_lengths(self, start: NodeT) -> dict[NodeT, float]:
        """Return the longest path length (sum of edge weights) from start to
        every node reachable from it. Unreached nodes map to ``float("-inf")``.

        Only valid for DAGs; relies on topological ordering, so raises
        ValueError if the graph contains a cycle.
        """
        order = self.topological_sort()
        distances: dict[NodeT, float] = dict.fromkeys(self._adjacency, float("-inf"))
        distances[start] = 0

        for node in order:
            if distances[node] == float("-inf"):
                continue
            for neighbor, weight in self._adjacency.get(node, {}).items():
                candidate = distances[node] + weight
                if candidate > distances[neighbor]:
                    distances[neighbor] = candidate

        return distances

    def shortest_path_lengths(self, start: NodeT) -> dict[NodeT, float]:
        """Return the shortest path length (sum of edge weights) from start to
        every node reachable from it. Unreached nodes map to ``float("inf")``.

        Only valid for DAGs; relies on topological ordering, so raises
        ValueError if the graph contains a cycle.
        """
        order = self.topological_sort()
        distances: dict[NodeT, float] = dict.fromkeys(self._adjacency, float("inf"))
        distances[start] = 0

        for node in order:
            if distances[node] == float("inf"):
                continue
            for neighbor, weight in self._adjacency.get(node, {}).items():
                candidate = distances[node] + weight
                if candidate < distances[neighbor]:
                    distances[neighbor] = candidate

        return distances

    def __repr__(self) -> str:
        return f"Graph(nodes={len(self._adjacency)}, edges={len(self.edges())})"

    def __contains__(self, node: NodeT) -> bool:
        return node in self._adjacency

    def __len__(self) -> int:
        return len(self._adjacency)
