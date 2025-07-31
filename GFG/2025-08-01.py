class Solution:
    def countBalanced(self, arr):
        from collections import defaultdict

        def get_balance(s):
            vowels = set('aeiou')
            bal = 0
            for ch in s:
                if ch in vowels:
                    bal += 1
                else:
                    bal -= 1
            return bal

        count = 0
        balance = 0
        balance_map = defaultdict(int)
        balance_map[0] = 1  

        for s in arr:
            balance += get_balance(s)
            count += balance_map[balance]
            balance_map[balance] += 1

        return count
