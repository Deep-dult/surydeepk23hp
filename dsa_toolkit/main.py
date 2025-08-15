import argparse
from typing import List

from .datastructures import Stack, Queue, LinkedList, BinarySearchTree, MinHeap, Trie, UnionFind
from .algorithms import (
	merge_sort,
	quick_sort,
	heap_sort,
	Graph,
	bfs,
	dfs,
	dijkstra,
	topological_sort,
	kmp_search,
	kmp_find_all,
	knapsack_01,
	lis_length,
	coin_change_min_coins,
)


def parse_int_list(values: List[str]) -> List[int]:
	return [int(v) for v in values]


def cmd_demo():
	print("Stack demo:")
	s = Stack()
	for v in [1, 2, 3]:
		s.push(v)
	print("pop ->", s.pop())

	print("Queue demo:")
	q = Queue()
	for v in [1, 2, 3]:
		q.enqueue(v)
	print("dequeue ->", q.dequeue())

	print("LinkedList demo:")
	ll = LinkedList()
	ll.append(1); ll.append(2); ll.prepend(0)
	print("contains 2 ->", ll.find(2) is not None)

	print("BST inorder:")
	bst = BinarySearchTree()
	for v in [5, 2, 7, 1, 3, 6, 8]:
		bst.insert(v)
	print(bst.inorder())

	print("MinHeap demo:")
	h = MinHeap()
	for v in [5, 3, 8, 1]:
		h.push(v)
	print([h.pop() for _ in range(len(h))])

	print("Trie suggestions for prefix 'ap':")
	trie = Trie()
	for w in ["apple", "apply", "apt", "cat", "cap", "dog"]:
		trie.insert(w)
	print(trie.suggest("ap", limit=10))

	print("Union-Find connectivity:")
	uf = UnionFind(5)
	uf.union(0, 1); uf.union(1, 2)
	print("0~2:", uf.connected(0, 2), "0~3:", uf.connected(0, 3))

	print("Sorting quick_sort:", quick_sort([5, 3, 8, 1]))

	print("Graph Dijkstra A->C:")
	g = Graph(directed=False)
	g.add_edge("A", "B", 1)
	g.add_edge("B", "C", 2)
	g.add_edge("A", "C", 10)
	d, path = dijkstra(g, "A", "C")
	print(d, path)

	print("KMP find 'ana' in 'bananana':", kmp_find_all("bananana", "ana"))

	print("DP knapsack_01:", knapsack_01([2,3,4], [4,5,10], 5))
	print("LIS length:", lis_length([10,9,2,5,3,7,101,18]))
	print("Coin change min coins:", coin_change_min_coins([1,2,5], 11))


def build_parser():
	parser = argparse.ArgumentParser(description="DSA Toolkit CLI")
	sub = parser.add_subparsers(dest="command")

	sub.add_parser("demo", help="Run the demo")

	# sort
	p_sort = sub.add_parser("sort", help="Sort values with selected algorithm")
	p_sort.add_argument("--algo", choices=["merge", "quick", "heap"], required=True)
	p_sort.add_argument("--values", nargs='+', required=True)

	# graph
	p_graph = sub.add_parser("graph", help="Graph algorithms")
	sub_graph = p_graph.add_subparsers(dest="graph_cmd")
	p_dij = sub_graph.add_parser("dijkstra", help="Run Dijkstra shortest path")
	p_dij.add_argument("--edges", nargs='+', help="Edges as 'u v w'", required=True)
	p_dij.add_argument("--source", required=True)
	p_dij.add_argument("--target", required=True)

	# trie
	p_trie = sub.add_parser("trie", help="Trie operations")
	sub_trie = p_trie.add_subparsers(dest="trie_cmd")
	p_suggest = sub_trie.add_parser("suggest", help="Autocomplete suggestions")
	p_suggest.add_argument("--words", nargs='+', required=True)
	p_suggest.add_argument("--prefix", required=True)
	p_suggest.add_argument("--limit", type=int, default=10)

	# bst traversal
	p_bst = sub.add_parser("bst", help="BST traversals")
	sub_bst = p_bst.add_subparsers(dest="bst_cmd")
	p_bst_in = sub_bst.add_parser("inorder", help="Inorder traversal")
	p_bst_in.add_argument("--values", nargs='+', required=True)

	# dsu
	p_dsu = sub.add_parser("dsu", help="Disjoint Set (Union-Find)")
	p_dsu.add_argument("--size", type=int, required=True)
	p_dsu.add_argument("--unions", nargs='*', default=[])
	p_dsu.add_argument("--queries", nargs='*', default=[])

	return parser


def handle_sort(args):
	values = parse_int_list(args.values)
	if args.algo == "merge":
		print(merge_sort(values))
	elif args.algo == "quick":
		print(quick_sort(values))
	else:
		print(heap_sort(values))


def handle_graph_dijkstra(args):
	g = Graph(directed=False)
	for e in args.edges:
		u, v, w = e.split()
		g.add_edge(u, v, int(w))
	d, path = dijkstra(g, args.source, args.target)
	print(d, path)


def handle_trie_suggest(args):
	trie = Trie()
	for w in args.words:
		trie.insert(w)
	print(trie.suggest(args.prefix, args.limit))


def handle_bst_inorder(args):
	bst = BinarySearchTree()
	for v in parse_int_list(args.values):
		bst.insert(v)
	print(bst.inorder())


def handle_dsu(args):
	uf = UnionFind(args.size)
	for pair in args.unions:
		a, b = pair.split('-')
		uf.union(int(a), int(b))
	for pair in args.queries:
		a, b = pair.split('-')
		print(int(a), int(b), uf.connected(int(a), int(b)))


def main():
	parser = build_parser()
	args, unknown = parser.parse_known_args()
	if args.command == "demo":
		cmd_demo()
		return
	if args.command == "sort":
		handle_sort(args)
	elif args.command == "graph" and args.graph_cmd == "dijkstra":
		handle_graph_dijkstra(args)
	elif args.command == "trie" and args.trie_cmd == "suggest":
		handle_trie_suggest(args)
	elif args.command == "bst" and args.bst_cmd == "inorder":
		handle_bst_inorder(args)
	elif args.command == "dsu":
		handle_dsu(args)
	else:
		parser.print_help()


if __name__ == "__main__":
	main()