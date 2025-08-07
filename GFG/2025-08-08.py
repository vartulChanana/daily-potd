class Solution:
    def getLPSLength(self, s):
        n = len(s)
        lps = [0] * n
        length = 0  # length of the previous longest prefix suffix

        # loop from index 1 to n-1
        i = 1
        while i < n:
            if s[i] == s[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]  # backtrack
                else:
                    lps[i] = 0
                    i += 1

        return lps[-1] if lps[-1] != n else lps[-1] - 1  # avoid full string match
