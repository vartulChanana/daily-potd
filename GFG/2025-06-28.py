from bisect import bisect_right
class Solution:
    def countLessEq(self, a, b):
        b.sort()
        result = []
        for num in a:
            count = bisect_right(b, num)
            result.append(count)
        return result
