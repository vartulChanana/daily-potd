import heapq
from typing import List

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Helper to calculate gain if we add one extra student
        def gain(p: int, t: int) -> float:
            return (p + 1) / (t + 1) - p / t

        # Max heap: store (-gain, pass, total) because Python heapq is a min-heap
        heap = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)

        # Assign extra students one by one
        for _ in range(extraStudents):
            g, p, t = heapq.heappop(heap)  # pick class with max gain
            p, t = p + 1, t + 1           # add one student
            heapq.heappush(heap, (-gain(p, t), p, t))

        # Compute the final average pass ratio
        return sum(p / t for _, p, t in heap) / len(classes)
