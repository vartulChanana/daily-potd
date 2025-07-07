class Solution:
    def nextLargerElement(self, arr):
        n = len(arr)
        res = [-1] * n
        stack = []

        for i in range(2 * n - 1, -1, -1):
            current = arr[i % n]
            while stack and stack[-1] <= current:
                stack.pop()
            if i < n:
                if stack:
                    res[i] = stack[-1]
            stack.append(current)

        return res
