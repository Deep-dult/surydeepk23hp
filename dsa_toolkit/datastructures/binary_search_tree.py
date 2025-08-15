class _BSTNode:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None


class BinarySearchTree:
	def __init__(self):
		self.root = None

	def insert(self, key):
		self.root = self._insert(self.root, key)

	def _insert(self, node, key):
		if node is None:
			return _BSTNode(key)
		if key < node.key:
			node.left = self._insert(node.left, key)
		elif key > node.key:
			node.right = self._insert(node.right, key)
		return node

	def contains(self, key):
		return self._contains(self.root, key)

	def _contains(self, node, key):
		if node is None:
			return False
		if key == node.key:
			return True
		if key < node.key:
			return self._contains(node.left, key)
		return self._contains(node.right, key)

	def delete(self, key):
		self.root = self._delete(self.root, key)

	def _delete(self, node, key):
		if node is None:
			return None
		if key < node.key:
			node.left = self._delete(node.left, key)
		elif key > node.key:
			node.right = self._delete(node.right, key)
		else:
			if node.left is None:
				return node.right
			if node.right is None:
				return node.left
			min_larger = self._min_node(node.right)
			node.key = min_larger.key
			node.right = self._delete(node.right, min_larger.key)
		return node

	def _min_node(self, node):
		current = node
		while current.left is not None:
			current = current.left
		return current

	def inorder(self):
		result = []
		self._inorder(self.root, result)
		return result

	def _inorder(self, node, result):
		if node is None:
			return
		self._inorder(node.left, result)
		result.append(node.key)
		self._inorder(node.right, result)

	def preorder(self):
		result = []
		self._preorder(self.root, result)
		return result

	def _preorder(self, node, result):
		if node is None:
			return
		result.append(node.key)
		self._preorder(node.left, result)
		self._preorder(node.right, result)

	def postorder(self):
		result = []
		self._postorder(self.root, result)
		return result

	def _postorder(self, node, result):
		if node is None:
			return
		self._postorder(node.left, result)
		self._postorder(node.right, result)
		result.append(node.key)