class Stack:
	def __init__(self):
		self._data = []

	def push(self, value):
		self._data.append(value)

	def pop(self):
		if not self._data:
			raise IndexError("pop from empty stack")
		return self._data.pop()

	def peek(self):
		if not self._data:
			raise IndexError("peek from empty stack")
		return self._data[-1]

	def is_empty(self):
		return len(self._data) == 0

	def size(self):
		return len(self._data)