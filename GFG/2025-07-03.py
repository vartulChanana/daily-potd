class Solution:
    def longestKSubstr(self, s, k):
        n = len(s)
        if n == 0 or k == 0:
            return -1
        
        left = 0
        max_len = -1
        char_map = {}
        
        for right in range(n):
            char_map[s[right]] = char_map.get(s[right], 0) + 1
            
            while len(char_map) > k:
                char_map[s[left]] -= 1
                if char_map[s[left]] == 0:
                    del char_map[s[left]]
                left += 1
            
            if len(char_map) == k:
                max_len = max(max_len, right - left + 1)
        
        return max_len
