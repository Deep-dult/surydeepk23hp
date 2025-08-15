class LinkedListNode:
	def __init__(self, value, next_node=None):
		self.value = value
		self.next = next_node


class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self._size = 0

	def append(self, value):
		node = LinkedListNode(value)
		if self.tail is None:
			self.head = self.tail = node
		else:
			self.tail.next = node
			self.tail = node
		self._size += 1

	def prepend(self, value):
		node = LinkedListNode(value, self.head)
		self.head = node
		if self.tail is None:
			self.tail = node
		self._size += 1

	def find(self, value):
		current = self.head
		while current:
			if current.value == value:
				return current
			current = current.next
		return None

	def delete(self, value):
		prev = None
		current = self.head
		while current:
			if current.value == value:
				if prev is None:
					self.head = current.next
				else:
					prev.next = current.next
				if current is self.tail:
					self.tail = prev
				self._size -= 1
				return True
			prev = current
			current = current.next
		return False

	def __iter__(self):
		current = self.head
		while current:
			yield current.value
			current = current.next

	def __len__(self):
		return self._size