class Solution:
    def substrCount(self, s, k):
        count = 0
        n = len(s)
        
        for i in range(n - k + 1):
            substring = s[i:i + k]
            distinct_chars = set(substring)
            if len(distinct_chars) == k - 1:
                count += 1
        
        return count
