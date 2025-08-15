class _TrieNode:
	def __init__(self):
		self.children = {}
		self.is_end = False


class Trie:
	def __init__(self):
		self.root = _TrieNode()

	def insert(self, word):
		node = self.root
		for ch in word:
			node = node.children.setdefault(ch, _TrieNode())
		node.is_end = True

	def contains(self, word):
		node = self.root
		for ch in word:
			if ch not in node.children:
				return False
			node = node.children[ch]
		return node.is_end

	def starts_with(self, prefix):
		node = self.root
		for ch in prefix:
			if ch not in node.children:
				return []
			node = node.children[ch]
		result = []
		self._collect(node, prefix, result)
		return result

	def suggest(self, prefix, limit=10):
		return self.starts_with(prefix)[:limit]

	def _collect(self, node, path, result):
		if node.is_end:
			result.append(path)
		for ch, child in node.children.items():
			self._collect(child, path + ch, result)