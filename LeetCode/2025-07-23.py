class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pair(s: str, first: str, second: str, gain: int):
            stack = []
            points = 0
            for char in s:
                if stack and stack[-1] == first and char == second:
                    stack.pop()
                    points += gain
                else:
                    stack.append(char)
            return ''.join(stack), points

        total_points = 0

        # First remove the more valuable substring
        if x >= y:
            s, gain = remove_pair(s, 'a', 'b', x)
            total_points += gain
            _, gain = remove_pair(s, 'b', 'a', y)
            total_points += gain
        else:
            s, gain = remove_pair(s, 'b', 'a', y)
            total_points += gain
            _, gain = remove_pair(s, 'a', 'b', x)
            total_points += gain

        return total_points
