from typing import List

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        
        # Step 1: Build powers[] from bits of n
        powers = []
        bit = 0
        while n > 0:
            if n & 1:
                powers.append(1 << bit)
            n >>= 1
            bit += 1
        
        # Step 2: Prefix products
        m = len(powers)
        prefix = [1] * (m + 1)
        for i in range(m):
            prefix[i+1] = (prefix[i] * powers[i]) % MOD
        
        # Step 3: Answer queries
        ans = []
        for l, r in queries:
            prod = prefix[r+1] * pow(prefix[l], MOD-2, MOD) % MOD
            ans.append(prod)
        
        return ans
