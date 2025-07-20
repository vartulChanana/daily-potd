class Solution:
    def countValid(self, n, arr):
        arr_set = set(arr)
        all_digits = set(range(10))
        allowed = list(all_digits - arr_set)

        if not allowed:
            return 0

        total = 9 * (10 ** (n - 1))
        count = 0

        for digit in allowed:
            if digit == 0:
                continue
            count += 1

        if count == 0:
            return total

        without_arr = count * (len(allowed) ** (n - 1))
        return total - without_arr
