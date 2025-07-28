from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        max_or = 0
        count = 0

        def dfs(i, curr_or):
            nonlocal max_or, count
            if i == n:
                if curr_or == max_or:
                    count += 1
                elif curr_or > max_or:
                    max_or = curr_or
                    count = 1
                return
            
            # include nums[i]
            dfs(i + 1, curr_or | nums[i])
            # exclude nums[i]
            dfs(i + 1, curr_or)

        dfs(0, 0)
        return count
