class MinHeap:
	def __init__(self):
		self._data = []

	def push(self, value):
		self._data.append(value)
		self._sift_up(len(self._data) - 1)

	def pop(self):
		if not self._data:
			raise IndexError("pop from empty heap")
		self._swap(0, len(self._data) - 1)
		min_value = self._data.pop()
		if self._data:
			self._sift_down(0)
		return min_value

	def peek(self):
		if not self._data:
			raise IndexError("peek from empty heap")
		return self._data[0]

	def _sift_up(self, idx):
		while idx > 0:
			parent = (idx - 1) // 2
			if self._data[idx] < self._data[parent]:
				self._swap(idx, parent)
				idx = parent
			else:
				break

	def _sift_down(self, idx):
		n = len(self._data)
		while True:
			left = 2 * idx + 1
			right = 2 * idx + 2
			smallest = idx
			if left < n and self._data[left] < self._data[smallest]:
				smallest = left
			if right < n and self._data[right] < self._data[smallest]:
				smallest = right
			if smallest != idx:
				self._swap(idx, smallest)
				idx = smallest
			else:
				break

	def _swap(self, i, j):
		self._data[i], self._data[j] = self._data[j], self._data[i]

	def __len__(self):
		return len(self._data)