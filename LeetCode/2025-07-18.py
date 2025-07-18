from heapq import heappush, heappop
from typing import List

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        total = len(nums)

        # Prefix: Max sum of n elements from the first 2n elements
        max_heap = []
        left_sum = sum(nums[:n])
        left_sums = [0] * (total + 1)
        for i in range(n):
            heappush(max_heap, -nums[i])
        left_sums[n] = left_sum

        for i in range(n, 2 * n):
            heappush(max_heap, -nums[i])
            left_sum += nums[i] + heappop(max_heap)
            left_sums[i + 1] = left_sum

        # Suffix: Min sum of n elements from the last 2n elements
        min_heap = []
        right_sum = sum(nums[2 * n:])
        right_sums = [0] * (total + 1)
        for i in range(3 * n - 1, 2 * n - 1, -1):
            heappush(min_heap, nums[i])
        right_sums[2 * n] = right_sum

        for i in range(2 * n - 1, n - 1, -1):
            heappush(min_heap, nums[i])
            right_sum += nums[i] - heappop(min_heap)
            right_sums[i] = right_sum

        # Find minimum difference
        min_diff = float('inf')
        for i in range(n, 2 * n + 1):
            diff = left_sums[i] - right_sums[i]
            min_diff = min(min_diff, diff)

        return min_diff

