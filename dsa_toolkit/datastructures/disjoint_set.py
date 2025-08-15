class UnionFind:
	def __init__(self, size):
		self.parent = list(range(size))
		self.rank = [0] * size

	def find(self, x):
		if self.parent[x] != x:
			self.parent[x] = self.find(self.parent[x])
		return self.parent[x]

	def union(self, x, y):
		rx = self.find(x)
		ry = self.find(y)
		if rx == ry:
			return False
		if self.rank[rx] < self.rank[ry]:
			rx, ry = ry, rx
		self.parent[ry] = rx
		if self.rank[rx] == self.rank[ry]:
			self.rank[rx] += 1
		return True

	def connected(self, x, y):
		return self.find(x) == self.find(y)