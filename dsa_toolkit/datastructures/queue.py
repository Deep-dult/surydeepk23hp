from collections import deque


class Queue:
	def __init__(self):
		self._data = deque()

	def enqueue(self, value):
		self._data.append(value)

	def dequeue(self):
		if not self._data:
			raise IndexError("dequeue from empty queue")
		return self._data.popleft()

	def peek(self):
		if not self._data:
			raise IndexError("peek from empty queue")
		return self._data[0]

	def is_empty(self):
		return len(self._data) == 0

	def size(self):
		return len(self._data)