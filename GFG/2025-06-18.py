class Solution:
    def is_palindrome(self, s):
        return s == s[::-1]

    def backtrack(self, start, s, path, result):
        if start == len(s):
            result.append(path.copy())
            return
        
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if self.is_palindrome(substring):
                path.append(substring)
                self.backtrack(end, s, path, result)
                path.pop()  

    def palinParts(self, s):
        result = []
        self.backtrack(0, s, [], result)
        return result
