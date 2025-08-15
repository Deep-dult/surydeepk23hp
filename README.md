# DSA Toolkit (Python)

A compact, self-contained Data Structures and Algorithms (DSA) toolkit written in Python with a simple CLI for demos.

## Features
- Core data structures: Stack, Queue, Linked List, Binary Search Tree, Min Heap, Trie, Union-Find (Disjoint Set)
- Algorithms: Sorting (merge/quick/heap), Graphs (BFS/DFS/Dijkstra/Topological Sort), Strings (KMP), Dynamic Programming (0/1 Knapsack, LIS, Coin Change)
- CLI demos and small utilities

## Requirements
- Python 3.9+
- No external dependencies

## Quickstart
```bash
cd /workspace
python -m dsa_toolkit.main --help
python -m dsa_toolkit.main demo
```

### Examples
- Sorting
```bash
python -m dsa_toolkit.main sort --algo quick --values 5 3 8 1
```
- Dijkstra shortest path
```bash
python -m dsa_toolkit.main graph dijkstra \
  --edges "A B 1" "B C 2" "A C 10" --source A --target C
```
- Trie suggestions
```bash
python -m dsa_toolkit.main trie suggest --words apple apply apt cat cap dog --prefix ap --limit 5
```
- BST traversal
```bash
python -m dsa_toolkit.main bst inorder --values 5 2 7 1 3 6 8
```
- Disjoint Set connectivity
```bash
python -m dsa_toolkit.main dsu --size 5 --unions 0-1 1-2 --queries 0-2 0-3
```

## Project Layout
```
dsa_toolkit/
  algorithms/
    sorting.py, graphs.py, strings.py, dp.py
  datastructures/
    stack.py, queue.py, linked_list.py, binary_search_tree.py, heap.py, trie.py, disjoint_set.py
  main.py
```

## License
MIT
