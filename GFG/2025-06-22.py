class Solution:
    def largestSubset(self, arr):
        n = len(arr)
        if n == 0:
            return []

        arr.sort()
        dp = [1] * n
        prev = [-1] * n
        paths = [[arr[i]] for i in range(n)]

        max_path = []

        for i in range(n):
            for j in range(i):
                if arr[i] % arr[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
                        paths[i] = paths[j] + [arr[i]]
                    elif dp[j] + 1 == dp[i]:
                        candidate = paths[j] + [arr[i]]
                        if candidate > paths[i]:
                            paths[i] = candidate
                            prev[i] = j

            if len(paths[i]) > len(max_path):
                max_path = paths[i]
            elif len(paths[i]) == len(max_path):
                if paths[i] > max_path:
                    max_path = paths[i]

        return max_path
