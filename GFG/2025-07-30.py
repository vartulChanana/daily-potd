class Solution:
    def cntSubarrays(self, arr, k):
        prefix_count = {0: 1}  # base case
        prefix_sum = 0
        count = 0
        
        for num in arr:
            prefix_sum += num
            if (prefix_sum - k) in prefix_count:
                count += prefix_count[prefix_sum - k]
            prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1
        
        return count
