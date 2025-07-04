class Solution:
    def maxSum(self, arr):
        max_score = 0
        n = len(arr)

        for i in range(n - 1):
            score = arr[i] + arr[i + 1]
            if score > max_score:
                max_score = score

        return max_score
