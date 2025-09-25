class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        res = []
        
        # Handle sign
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")
        
        # Work with positive values
        numerator, denominator = abs(numerator), abs(denominator)
        
        # Integer part
        integer_part = numerator // denominator
        res.append(str(integer_part))
        
        remainder = numerator % denominator
        if remainder == 0:
            return "".join(res)  # no fractional part
        
        res.append(".")
        
        # Dictionary to store seen remainders and their positions
        remainder_map = {}
        
        while remainder != 0:
            if remainder in remainder_map:
                # Insert parentheses at the repeating position
                res.insert(remainder_map[remainder], "(")
                res.append(")")
                break
            
            remainder_map[remainder] = len(res)
            
            remainder *= 10
            res.append(str(remainder // denominator))
            remainder %= denominator
        
        return "".join(res)
