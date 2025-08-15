from typing import List
from ..datastructures.heap import MinHeap


def merge_sort(values: List[int]) -> List[int]:
	if len(values) <= 1:
		return list(values)
	mid = len(values) // 2
	left = merge_sort(values[:mid])
	right = merge_sort(values[mid:])
	return _merge(left, right)


def _merge(left: List[int], right: List[int]) -> List[int]:
	result = []
	i = j = 0
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	result.extend(left[i:])
	result.extend(right[j:])
	return result


def quick_sort(values: List[int]) -> List[int]:
	arr = list(values)
	_quick_sort_inplace(arr, 0, len(arr) - 1)
	return arr


def _quick_sort_inplace(arr: List[int], lo: int, hi: int) -> None:
	if lo >= hi:
		return
	p = _partition(arr, lo, hi)
	_quick_sort_inplace(arr, lo, p - 1)
	_quick_sort_inplace(arr, p + 1, hi)


def _partition(arr: List[int], lo: int, hi: int) -> int:
	pivot = arr[hi]
	i = lo
	for j in range(lo, hi):
		if arr[j] <= pivot:
			arr[i], arr[j] = arr[j], arr[i]
			i += 1
	arr[i], arr[hi] = arr[hi], arr[i]
	return i


def heap_sort(values: List[int]) -> List[int]:
	heap = MinHeap()
	for v in values:
		heap.push(v)
	result = []
	while len(heap) > 0:
		result.append(heap.pop())
	return result