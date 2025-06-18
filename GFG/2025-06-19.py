class Solution:
    def caseSort(self, s):
        upper_chars = sorted([c for c in s if c.isupper()])
        lower_chars = sorted([c for c in s if c.islower()])
        
        upper_iter = iter(upper_chars)
        lower_iter = iter(lower_chars)
        
        result = []
        for c in s:
            if c.isupper():
                result.append(next(upper_iter))
            else:
                result.append(next(lower_iter))
        
        return ''.join(result)
