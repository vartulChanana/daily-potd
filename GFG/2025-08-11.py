class Solution:
    def maxSum(self, s: str) -> int:
        n = len(s)
        if n < 2: 
            return 0

        # Manacher odd-length (d1[i] = radius k where palindrome length = 2*k-1)
        d1 = [0] * n
        l, r = 0, -1
        for i in range(n):
            k = 1 if i > r else min(d1[l + r - i], r - i + 1)
            while i - k >= 0 and i + k < n and s[i - k] == s[i + k]:
                k += 1
            d1[i] = k
            if i + k - 1 > r:
                l, r = i - k + 1, i + k - 1

        # DSU helper
        def fill_by_centers(forward=True):
            nxt = list(range(n + 1))
            def find(x):
                while nxt[x] != x:
                    nxt[x] = nxt[nxt[x]]
                    x = nxt[x]
                return x
            res = [-1] * n
            if forward:
                # assign each end position the leftmost center that covers it
                for center in range(n):
                    end = center + d1[center] - 1
                    pos = find(center)
                    while pos <= end:
                        res[pos] = center
                        nxt[pos] = pos + 1
                        pos = find(pos)
            else:
                # assign each start position the rightmost center that covers it
                for center in range(n - 1, -1, -1):
                    start = center - (d1[center] - 1)
                    pos = find(start)
                    while pos <= center:
                        res[pos] = center
                        nxt[pos] = pos + 1
                        pos = find(pos)
            return res

        min_center_for_end = fill_by_centers(forward=True)
        max_center_for_start = fill_by_centers(forward=False)

        left = [0] * n
        for e in range(n):
            c = min_center_for_end[e]
            if c != -1:
                left[e] = 2 * (e - c) + 1
        for i in range(1, n):
            if left[i - 1] > left[i]:
                left[i] = left[i - 1]

        right = [0] * n
        for st in range(n):
            c = max_center_for_start[st]
            if c != -1:
                right[st] = 2 * (c - st) + 1
        for i in range(n - 2, -1, -1):
            if right[i + 1] > right[i]:
                right[i] = right[i + 1]

        ans = 0
        for i in range(n - 1):
            ans = max(ans, left[i] + right[i + 1])
        return ans
