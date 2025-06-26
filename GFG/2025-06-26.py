from collections import Counter
import heapq

class Solution:
    def minValue(self, s, k):
        freq = Counter(s)
        max_heap = [-f for f in freq.values()]
        heapq.heapify(max_heap)
        
        for _ in range(k):
            if max_heap:
                highest_freq = -heapq.heappop(max_heap)
                if highest_freq > 1:
                    heapq.heappush(max_heap, -(highest_freq - 1))
        
        min_value = sum((-f) ** 2 for f in max_heap)
        return min_value
