class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        count_zeros = s.count('0')
        count_ones = s.count('1')

        if k == 0:
            return count_zeros

        binary_number = 0
        length_of_subsequence = 0

        for char in reversed(s):
            if char == '1':
                if binary_number + (1 << length_of_subsequence) <= k:
                    binary_number += (1 << length_of_subsequence)
                    length_of_subsequence += 1
            else:
                length_of_subsequence += 1

        return length_of_subsequence
