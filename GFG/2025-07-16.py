import math

class Solution:
    def countNumbers(self, n):
        limit = int(n**0.5) + 1

        # Sieve of Eratosthenes to get all primes up to sqrt(n)
        is_prime = [True] * (limit)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(limit**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, limit, i):
                    is_prime[j] = False
        primes = [i for i, val in enumerate(is_prime) if val]

        count = 0

        # Case 1: Numbers of the form p^8
        for p in primes:
            if p**8 <= n:
                count += 1
            else:
                break

        # Case 2: Numbers of the form p1^2 * p2^2
        num_primes = len(primes)
        for i in range(num_primes):
            for j in range(i + 1, num_primes):
                val = primes[i]**2 * primes[j]**2
                if val <= n:
                    count += 1
                else:
                    break

        return count
