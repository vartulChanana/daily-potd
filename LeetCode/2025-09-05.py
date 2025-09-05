class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(1, 61):  # try from 1 to 60 operations
            target = num1 - k * num2
            if target < k:  # must be >= k
                continue
            # check if target can be expressed as sum of k powers of 2
            if bin(target).count("1") <= k:
                return k
        return -1
