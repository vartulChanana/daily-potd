from collections import Counter

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = Counter(word)
        frequencies = sorted(freq.values())
        min_deletions = float('inf')
        
        for i in range(len(frequencies)):
            target = frequencies[i]
            deletions = 0
            
            for f in frequencies:
                if f < target:
                    deletions += f
                elif f > target + k:
                    deletions += f - (target + k)
            
            min_deletions = min(min_deletions, deletions)
        
        return min_deletions
