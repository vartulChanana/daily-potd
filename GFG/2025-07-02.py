class Solution:
    def totalElements(self, arr):
        left = 0
        right = 0
        max_length = 0
        count_map = {}

        while right < len(arr):
            if arr[right] in count_map:
                count_map[arr[right]] += 1
            else:
                count_map[arr[right]] = 1
            
            while len(count_map) > 2:
                count_map[arr[left]] -= 1
                if count_map[arr[left]] == 0:
                    del count_map[arr[left]]
                left += 1
            
            max_length = max(max_length, right - left + 1)
            right += 1
        
        return max_length
