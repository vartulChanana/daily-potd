class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Power of two must be positive and have exactly one bit set
        return n > 0 and (n & (n - 1)) == 0
