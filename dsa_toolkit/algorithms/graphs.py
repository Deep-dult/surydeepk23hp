from collections import defaultdict, deque
from typing import Dict, List, Tuple, Any, Set
import heapq


class Graph:
	def __init__(self, directed: bool = False):
		self.directed = directed
		self.adj: Dict[Any, List[Tuple[Any, int]]] = defaultdict(list)

	def add_edge(self, u: Any, v: Any, w: int = 1) -> None:
		self.adj[u].append((v, w))
		if not self.directed:
			self.adj[v].append((u, w))

	def nodes(self) -> Set[Any]:
		nodes_set: Set[Any] = set(self.adj.keys())
		for u in self.adj:
			for v, _ in self.adj[u]:
				nodes_set.add(v)
		return nodes_set


def bfs(graph: Graph, start: Any) -> List[Any]:
	visited = set([start])
	order = []
	q = deque([start])
	while q:
		u = q.popleft()
		order.append(u)
		for v, _ in graph.adj.get(u, []):
			if v not in visited:
				visited.add(v)
				q.append(v)
	return order


def dfs(graph: Graph, start: Any) -> List[Any]:
	visited = set()
	order = []

	def _dfs(u):
		visited.add(u)
		order.append(u)
		for v, _ in graph.adj.get(u, []):
			if v not in visited:
				_dfs(v)

	_dfs(start)
	return order


def dijkstra(graph: Graph, source: Any, target: Any):
	dist = {node: float('inf') for node in graph.nodes()}
	prev = {node: None for node in graph.nodes()}
	dist[source] = 0
	pq = [(0, source)]
	while pq:
		d, u = heapq.heappop(pq)
		if d != dist[u]:
			continue
		if u == target:
			break
		for v, w in graph.adj.get(u, []):
			nd = d + w
			if nd < dist[v]:
				dist[v] = nd
				prev[v] = u
				heapq.heappush(pq, (nd, v))
	path = []
	u = target
	if dist.get(u, float('inf')) == float('inf'):
		return float('inf'), []
	while u is not None:
		path.append(u)
		u = prev[u]
	path.reverse()
	return dist[target], path


def topological_sort(graph: Graph) -> List[Any]:
	if not graph.directed:
		raise ValueError("Topological sort requires a directed graph")
	in_deg = {node: 0 for node in graph.nodes()}
	for u in graph.adj:
		for v, _ in graph.adj[u]:
			in_deg[v] = in_deg.get(v, 0) + 1
	q = deque([n for n, d in in_deg.items() if d == 0])
	order = []
	while q:
		u = q.popleft()
		order.append(u)
		for v, _ in graph.adj.get(u, []):
			in_deg[v] -= 1
			if in_deg[v] == 0:
				q.append(v)
	if len(order) != len(in_deg):
		raise ValueError("Graph has a cycle")
	return order