from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result = 0
        zero_count = 0
        
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                # End of consecutive zeros sequence
                if zero_count > 0:
                    # Add contribution of this sequence: k * (k + 1) / 2
                    result += zero_count * (zero_count + 1) // 2
                    zero_count = 0
        
        # Handle case where array ends with zeros
        if zero_count > 0:
            result += zero_count * (zero_count + 1) // 2
            
        return result
