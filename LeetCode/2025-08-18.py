class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def dfs(nums):
            # If only one number left, check if it's close to 24
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6
            
            # Try every pair of numbers
            n = len(nums)
            for i in range(n):
                for j in range(i+1, n):
                    a, b = nums[i], nums[j]
                    
                    # possible results of combining a and b
                    results = [a+b, a-b, b-a, a*b]
                    if abs(b) > 1e-6:  # avoid division by 0
                        results.append(a/b)
                    if abs(a) > 1e-6:
                        results.append(b/a)
                    
                    # remaining numbers (excluding a, b)
                    next_nums = [nums[k] for k in range(n) if k != i and k != j]
                    
                    # try each result with remaining numbers
                    for val in results:
                        if dfs(next_nums + [val]):
                            return True
            return False
        
        return dfs([float(x) for x in cards])
