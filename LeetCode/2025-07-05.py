class Solution:
    def findLucky(self, arr):
        freq = {}
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        max_lucky = -1
        for num in freq:
            if freq[num] == num:
                max_lucky = max(max_lucky, num)

        return max_lucky
