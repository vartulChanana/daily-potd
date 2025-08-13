import math

class Solution:
    def minSoldiers(self, arr, k):
        n = len(arr)
        lucky_troops_needed = math.ceil(n / 2)
        costs = []
        for soldiers in arr:
            remainder = soldiers % k
            if remainder == 0:
                cost = 0  
            else:
                cost = k - remainder  # Need to add this many soldiers
            costs.append(cost)
        
        # Sort costs in ascending order to get minimum total cost
        costs.sort()
        
        # Take the sum of the smallest lucky_troops_needed costs
        return sum(costs[:lucky_troops_needed])

