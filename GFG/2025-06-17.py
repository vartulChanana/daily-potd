class Solution:
    def minCost(self, heights, cost):
        def calculate_cost(target_height):
            total_cost = 0
            for h, c in zip(heights, cost):
                total_cost += abs(h - target_height) * c
            return total_cost

        low, high = min(heights), max(heights)
        min_cost = float('inf')

        while low <= high:
            mid = (low + high) // 2
            cost_mid = calculate_cost(mid)
            cost_mid_plus_one = calculate_cost(mid + 1)

            min_cost = min(min_cost, cost_mid, cost_mid_plus_one)

            if cost_mid < cost_mid_plus_one:
                high = mid - 1
            else:
                low = mid + 1

        return min_cost



