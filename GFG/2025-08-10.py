class Solution:
    def countPS(self, s):
        n = len(s)
        count = 0
        
        def expand(l, r):
            nonlocal count
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 >= 2:
                    count += 1
                l -= 1
                r += 1
        
        i = 0
        while i < n:
            # Handle odd length palindromes
            expand(i, i)
            
            # Handle even length blocks of same character efficiently
            j = i
            while j + 1 < n and s[j] == s[j + 1]:
                j += 1
            expand(i, j)
            
            i = j + 1
        
        return count
