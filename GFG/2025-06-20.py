from collections import Counter

class Solution:
    def validgroup(self, arr, k):
        if len(arr) % k != 0:
            return False
        
        count = Counter(arr)
        unique_numbers = sorted(count.keys())
        
        for num in unique_numbers:
            if count[num] > 0:
                num_groups = count[num]
                for i in range(num, num + k):
                    if count[i] < num_groups:
                        return False
                    count[i] -= num_groups
        
        return True
