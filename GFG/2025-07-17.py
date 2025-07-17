from collections import defaultdict

class Solution:
    def maxKPower(self, n, k):
        def prime_factors(k):
            factors = defaultdict(int)
            d = 2
            while d * d <= k:
                while k % d == 0:
                    factors[d] += 1
                    k //= d
                d += 1
            if k > 1:
                factors[k] += 1
            return factors

        def count_in_factorial(n, p):
            count = 0
            while n:
                n //= p
                count += n
            return count

        factors = prime_factors(k)
        min_x = float('inf')

        for prime, power in factors.items():
            count = count_in_factorial(n, prime)
            min_x = min(min_x, count // power)

        return min_x
