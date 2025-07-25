class Solution:
    def maxCircularSum(self, arr):
        def kadane(nums):
            max_end = max_so_far = nums[0]
            for num in nums[1:]:
                max_end = max(num, max_end + num)
                max_so_far = max(max_so_far, max_end)
            return max_so_far
        
        def min_kadane(nums):
            min_end = min_so_far = nums[0]
            for num in nums[1:]:
                min_end = min(num, min_end + num)
                min_so_far = min(min_so_far, min_end)
            return min_so_far
        
        total_sum = sum(arr)
        max_kadane = kadane(arr)
        min_kadane_sum = min_kadane(arr)
        
        if max_kadane < 0:
            return max_kadane
        
        max_wrap = total_sum - min_kadane_sum
        return max(max_kadane, max_wrap)
