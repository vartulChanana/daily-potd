class Solution:
    def minimumCoins(self, arr, k):
        arr.sort()
        n = len(arr)

        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + arr[i]

        min_removed = float('inf')

        for i in range(n):
            max_allowed = arr[i] + k

            low, high = i, n - 1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] <= max_allowed:
                    low = mid + 1
                else:
                    high = mid - 1

            removed = prefix_sum[i]
            if high + 1 < n:
                removed += prefix_sum[n] - prefix_sum[high + 1] - (n - high - 1) * (arr[i] + k)

            min_removed = min(min_removed, removed)

        return min_removed
