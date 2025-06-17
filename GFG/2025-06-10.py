from collections import Counter

class Solution:
    def countStrings(self, s):
        n = len(s)
        freq = Counter(s)
        
        total_pairs = n * (n - 1) // 2
        equal_char_pairs = 0
        
        for c in freq:
            f = freq[c]
            equal_char_pairs += f * (f - 1) // 2
        
        has_duplicates = any(f > 1 for f in freq.values())
        
        if has_duplicates:
            return 1 + total_pairs - equal_char_pairs
        else:
            return total_pairs
