class Solution:
    def findLength(self, color, radius):
        stack = []
        
        for i in range(len(color)):
            current_ball = (color[i], radius[i])
            
            if stack and stack[-1] == current_ball:
                stack.pop()
            else:
                stack.append(current_ball)
        
        return len(stack)
