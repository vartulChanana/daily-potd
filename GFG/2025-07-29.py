class Solution:
    def asciirange(self, s):
        first_pos = {}
        last_pos = {}

        # Record first and last positions
        for i, ch in enumerate(s):
            if ch not in first_pos:
                first_pos[ch] = i
            last_pos[ch] = i

        result = []

        for ch in first_pos:
            first = first_pos[ch]
            last = last_pos[ch]
            if first != last:
                # get substring between first and last (exclusive)
                ascii_sum = sum(ord(c) for c in s[first + 1:last])
                if ascii_sum > 0:
                    result.append(ascii_sum)

        return result
