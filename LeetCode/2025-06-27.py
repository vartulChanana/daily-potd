from collections import Counter

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        freq = Counter(s)
        chars = [c for c in sorted(freq.keys(), reverse=True) if freq[c] >= k]

        def is_valid(t):
            tk = t * k
            i = 0
            for ch in s:
                if i < len(tk) and tk[i] == ch:
                    i += 1
                if i == len(tk):
                    return True
            return i == len(tk)

        best = ""

        def dfs(path):
            nonlocal best
            if len(path) > 7:
                return
            if len(path) > len(best) or (len(path) == len(best) and path > best):
                if is_valid(path):
                    best = path
            for c in chars:
                new_path = path + c
                if is_valid(new_path):
                    dfs(new_path)

        dfs("")
        return best
