class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        groups = []
        i = 0

        while i < n:
            j = i
            while j < n and word[j] == word[i]:
                j += 1
            groups.append((word[i], j - i))
            i = j

        total = 1

        for idx, (char, length) in enumerate(groups):
            for reduce in range(1, length):
                new_groups = groups.copy()
                new_groups[idx] = (char, length - reduce)
                valid = True
                for c, l in new_groups:
                    if l <= 0:
                        valid = False
                        break
                if valid:
                    total += 1

        return total
