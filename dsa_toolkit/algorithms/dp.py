from typing import List


def knapsack_01(weights: List[int], values: List[int], capacity: int) -> int:
	n = len(weights)
	dp = [0] * (capacity + 1)
	for i in range(n):
		w = weights[i]
		v = values[i]
		for c in range(capacity, w - 1, -1):
			dp[c] = max(dp[c], dp[c - w] + v)
	return dp[capacity]


def lis_length(nums: List[int]) -> int:
	import bisect
	tails: List[int] = []
	for x in nums:
		i = bisect.bisect_left(tails, x)
		if i == len(tails):
			tails.append(x)
		else:
			tails[i] = x
	return len(tails)


def coin_change_min_coins(coins: List[int], amount: int) -> int:
	INF = 10**9
	dp = [0] + [INF] * amount
	for a in range(1, amount + 1):
		best = INF
		for c in coins:
			if c <= a and dp[a - c] + 1 < best:
				best = dp[a - c] + 1
		dp[a] = best
	return -1 if dp[amount] >= INF else dp[amount]