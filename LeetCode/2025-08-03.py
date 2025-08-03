from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        pos = [p for p, _ in fruits]
        prefix = [0] * (n + 1)
        
        for i in range(n):
            prefix[i + 1] = prefix[i] + fruits[i][1]
        
        def get_sum(l, r):
            return prefix[r + 1] - prefix[l]
        
        max_fruits = 0
        left = 0
        
        for right in range(n):
            # Expand window to right
            while left <= right:
                l_pos = fruits[left][0]
                r_pos = fruits[right][0]
                
                dist1 = abs(startPos - l_pos) + (r_pos - l_pos)  # left then right
                dist2 = abs(startPos - r_pos) + (r_pos - l_pos)  # right then left
                
                if min(dist1, dist2) <= k:
                    break
                left += 1  # Shrink window from left if too far
                
            # Now [left..right] is a valid window
            max_fruits = max(max_fruits, get_sum(left, right))
        
        return max_fruits
