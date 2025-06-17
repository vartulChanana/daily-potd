class Solution:
    def smallestDivisor(self, arr, k):
        def calculate_sum(divisor):
            return sum((num + divisor - 1) // divisor for num in arr)  # This computes the ceiling of num / divisor

        left, right = 1, max(arr)  # The smallest divisor can be at least 1 and at most the maximum element in arr
        while left < right:
            mid = (left + right) // 2
            if calculate_sum(mid) <= k:
                right = mid  # We can try for a smaller divisor
            else:
                left = mid + 1  # We need a larger divisor

        return left  # left will be the smallest divisor that satisfies the condition

