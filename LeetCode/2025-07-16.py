class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        max_length = 0
        
        for pattern in range(4):
            if pattern == 0:
                count = sum(1 for x in nums if x % 2 == 0)
            elif pattern == 1:
                count = sum(1 for x in nums if x % 2 == 1)
            elif pattern == 2:
                count = 0
                expected_parity = 0
                for x in nums:
                    if x % 2 == expected_parity:
                        count += 1
                        expected_parity = 1 - expected_parity
            else:
                count = 0
                expected_parity = 1
                for x in nums:
                    if x % 2 == expected_parity:
                        count += 1
                        expected_parity = 1 - expected_parity
            
            max_length = max(max_length, count)
        
        return max_length
