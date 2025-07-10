class Solution:
    def longestString(self, words):
        word_set = set(words)
        words.sort(key=lambda w: (-len(w), w))
        
        for word in words:
            all_prefixes_exist = True
            for i in range(1, len(word)):
                if word[:i] not in word_set:
                    all_prefixes_exist = False
                    break
            if all_prefixes_exist:
                return word
        return ""
