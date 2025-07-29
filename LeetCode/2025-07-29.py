class Solution:
    def smallestSubarrays(self, nums):
        n = len(nums)
        answer = [0] * n
        last_seen = [-1] * 32  # tracks last seen index for each bit (0 to 31)
        
        for i in range(n - 1, -1, -1):
            num = nums[i]
            for bit in range(32):
                if (num >> bit) & 1:
                    last_seen[bit] = i  # update the latest index where this bit is set
            
            # max index of any bit that contributes to OR
            max_len = i
            for j in range(32):
                if last_seen[j] != -1:
                    max_len = max(max_len, last_seen[j])
            answer[i] = max_len - i + 1  # length of subarray
        return answer
