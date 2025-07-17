from math import gcd

class Solution:
    def lcm(self, a, b):
        return a * b // gcd(a, b)

    def lcm3(self, a, b, c):
        return self.lcm(self.lcm(a, b), c)

    def lcmTriplets(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 6
        
        if n % 2 != 0:
            return self.lcm3(n, n-1, n-2)
        else:
            return max(
                self.lcm3(n, n-1, n-3),
                self.lcm3(n-1, n-2, n-3)
            )
