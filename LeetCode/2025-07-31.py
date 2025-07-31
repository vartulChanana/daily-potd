from typing import List

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()
        prev = set()
        
        for num in arr:
            # New set for ORs ending at this index
            curr = {num}
            for val in prev:
                curr.add(val | num)
            res.update(curr)
            prev = curr
        
        return len(res)
