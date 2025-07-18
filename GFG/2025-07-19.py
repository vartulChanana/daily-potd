from collections import Counter
from math import factorial
from functools import reduce
import operator

class Solution:
    def vowelCount(self, s):
        vowel_set = {'a', 'e', 'i', 'o', 'u'}
        counter = Counter(s)
        unique_vowels = [ch for ch in counter if ch in vowel_set]
        if not unique_vowels:
            return 0
        product = reduce(operator.mul, (counter[v] for v in unique_vowels), 1)
        perms = factorial(len(unique_vowels))
        return product * perms
