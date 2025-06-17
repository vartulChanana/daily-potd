class Solution:
    def maxDiff(self, num: int) -> int:
        str_num = str(num)

        def maximize(num_str):
            for digit in num_str:
                if digit != '9':
                    x = digit
                    break
            else:
                return int(num_str)
            
            return int(num_str.replace(x, '9'))
        
        def minimize(num_str):
            for digit in num_str:
                if digit != '0' and digit != '1':
                    x = digit
                    break
            else:
                if num_str[0] == '1':
                    return int(num_str)
                else:
                    return int(num_str.replace(num_str[0], '1'))
            
            if num_str[0] == x:
                return int(num_str.replace(x, '1'))
            else:
                return int(num_str.replace(x, '0'))

        max_num = maximize(str_num)
        min_num = minimize(str_num)
        
        return max_num - min_num
