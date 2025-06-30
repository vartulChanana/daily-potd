class Solution:
    def maxMinHeight(self, arr, k, w):
        def is_possible(target):
            n = len(arr)
            current_water = [0] * (n + 1)
            days_used = 0
            for i in range(n):
                if i > 0:
                    current_water[i] += current_water[i - 1]
                effective_height = arr[i] + current_water[i]
                if effective_height < target:
                    needed = target - effective_height
                    days_used += needed
                    if days_used > k:
                        return False
                    current_water[i] += needed
                    if i + w < n:
                        current_water[i + w] -= needed
            return days_used <= k

        left = min(arr)
        right = max(arr) + k
        answer = left
        while left <= right:
            mid = (left + right) // 2
            if is_possible(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1
        return answer
