class Solution:
    def romanToDecimal(self, s): 
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        n = len(s)
        
        for i in range(n):
            curr_value = roman_map[s[i]]
            next_value = roman_map[s[i+1]] if i+1 < n else 0
            
            if curr_value < next_value:
                total -= curr_value
            else:
                total += curr_value
                
        return total
