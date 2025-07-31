class Solution:
    def countBalanced(self, arr):
        from collections import defaultdict
        
        vowels = set('aeiou')
        balance_counter = defaultdict(int)
        balance_counter[0] = 1  # Initial neutral balance
        balance = 0
        result = 0
        
        for s in arr:
            for ch in s:
                if ch in vowels:
                    balance += 1
                else:
                    balance -= 1
                result += balance_counter[balance]
                balance_counter[balance] += 1
                
        return result
