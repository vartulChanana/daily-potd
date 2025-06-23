class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def is_k_palindrome(x):
            digits = []
            while x:
                digits.append(x % k)
                x //= k
            return digits == digits[::-1]

        def generate_palindromes():
            # 1-digit palindromes first
            for i in range(1, 10):
                yield i
            
            length = 2
            while True:
                half_len = (length + 1) // 2
                start = 10 ** (half_len - 1)
                end = 10 ** half_len
                for half in range(start, end):
                    s = str(half)
                    if length % 2 == 0:
                        full = int(s + s[::-1])
                    else:
                        full = int(s + s[-2::-1])
                    yield full
                length += 1

        count = 0
        total = 0
        for num in generate_palindromes():
            if is_k_palindrome(num):
                total += num
                count += 1
                if count == n:
                    break
        return total
