class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7

        fact = [1] * (n + 1)
        for i in range(2, n + 1):
            fact[i] = fact[i - 1] * i % MOD

        inv_fact = [1] * (n + 1)
        inv_fact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        def nCk(n, k):
            if k > n or k < 0:
                return 0
            return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

        if k == 0:
            return m * pow(m - 1, n - 1, MOD) % MOD

        choose_k = nCk(n - 1, k)
        remaining_pos = n - 1 - k
        ways_fill_remaining = pow(m - 1, remaining_pos, MOD)

        total = choose_k * ways_fill_remaining % MOD
        total = total * m % MOD

        return total
