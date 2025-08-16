class Solution:
    def maximum69Number (self, num: int) -> int:
        # Convert number to string to easily manipulate digits
        num_str = list(str(num))
        
        # Find the first '6' and change it to '9'
        for i in range(len(num_str)):
            if num_str[i] == '6':
                num_str[i] = '9'
                break  # only one change allowed, so stop after first replacement
        
        # Convert back to integer
        return int("".join(num_str))
