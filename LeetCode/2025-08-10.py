class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # Precompute all possible digit patterns for powers of two
        power_two_patterns = {''.join(sorted(str(1 << i))) for i in range(31)}
        
        # Check if n's sorted digits match any power-of-two pattern
        return ''.join(sorted(str(n))) in power_two_patterns
