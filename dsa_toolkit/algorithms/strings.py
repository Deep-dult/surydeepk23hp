from typing import List


def _kmp_prefix(pattern: str) -> List[int]:
	pi = [0] * len(pattern)
	j = 0
	for i in range(1, len(pattern)):
		while j > 0 and pattern[i] != pattern[j]:
			j = pi[j - 1]
		if pattern[i] == pattern[j]:
			j += 1
			pi[i] = j
	return pi


def kmp_search(text: str, pattern: str) -> int:
	if pattern == "":
		return 0
	pi = _kmp_prefix(pattern)
	j = 0
	for i, ch in enumerate(text):
		while j > 0 and ch != pattern[j]:
			j = pi[j - 1]
		if ch == pattern[j]:
			j += 1
			if j == len(pattern):
				return i - j + 1
	return -1


def kmp_find_all(text: str, pattern: str) -> List[int]:
	indices = []
	if pattern == "":
		return list(range(len(text) + 1))
	pi = _kmp_prefix(pattern)
	j = 0
	for i, ch in enumerate(text):
		while j > 0 and ch != pattern[j]:
			j = pi[j - 1]
		if ch == pattern[j]:
			j += 1
			if j == len(pattern):
				indices.append(i - j + 1)
				j = pi[j - 1]
	return indices