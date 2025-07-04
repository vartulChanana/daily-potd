from typing import List

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        lengths = [1]
        for op in operations:
            lengths.append(lengths[-1] * 2)
        
        c = 'a'
        for i in reversed(range(len(operations))):
            half = lengths[i]
            op = operations[i]
            
            if k <= half:
                continue
            else:
                k -= half
                if op == 1:
                    c = next_char(c)
        
        return c

def next_char(c):
    return chr((ord(c) - ord('a') + 1) % 26 + ord('a'))
