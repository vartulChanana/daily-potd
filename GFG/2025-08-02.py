
class Solution:
    def longestSubarray(self, arr, k):
        n = len(arr)
        prefix_sum = 0
        max_len = 0
        first_occurrence = {}

        for i in range(n):
            if arr[i] > k:
                prefix_sum += 1
            else:
                prefix_sum -= 1

            if prefix_sum > 0:
                max_len = i + 1
            else:
                if prefix_sum not in first_occurrence:
                    first_occurrence[prefix_sum] = i
                if (prefix_sum - 1) in first_occurrence:
                    length = i - first_occurrence[prefix_sum - 1]
                    max_len = max(max_len, length)

        return max_len
