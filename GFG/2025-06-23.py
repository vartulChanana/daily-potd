class Solution:
    def minSum(self, arr):
        arr.sort()
        
        num1 = []
        num2 = []
        
        for i in range(len(arr)):
            if i % 2 == 0:
                num1.append(str(arr[i]))
            else:
                num2.append(str(arr[i]))
        
        str_num1 = ''.join(num1).lstrip('0') or '0'
        str_num2 = ''.join(num2).lstrip('0') or '0'
        
        return self.addStrings(str_num1, str_num2)

    def addStrings(self, num1, num2):
        result = []
        carry = 0
        i, j = len(num1) - 1, len(num2) - 1
        
        while i >= 0 or j >= 0 or carry:
            digit1 = int(num1[i]) if i >= 0 else 0
            digit2 = int(num2[j]) if j >= 0 else 0
            
            total = digit1 + digit2 + carry
            result.append(str(total % 10))
            carry = total // 10
            
            i -= 1
            j -= 1
        
        return ''.join(result[::-1])
