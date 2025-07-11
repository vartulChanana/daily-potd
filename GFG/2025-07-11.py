class Solution:
    def countConsec(self, n: int) -> int:
        if n < 2:
            return 0

        a, b = 1, 1  # base case for length 1
        for _ in range(2, n+1):
            new_a = a + b
            new_b = a
            a, b = new_a, new_b

        no_consec = a + b
        total = 1 << n  # 2^n
        return total - no_consec
