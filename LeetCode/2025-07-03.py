class Solution:
    def kthCharacter(self, k: int) -> str:
        def next_char(c):
            return 'a' if c == 'z' else chr(ord(c) + 1)

        word = "a"
        while len(word) < k:
            new_part = ''.join(next_char(c) for c in word)
            word += new_part
        return word[k - 1]
