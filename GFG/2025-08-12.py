class Solution:
    def minMaxCandy(self, prices, k):
        prices.sort()
        n = len(prices)

        # Minimum cost: buy cheapest, take k most expensive free
        min_cost = 0
        left, right = 0, n - 1
        while left <= right:
            min_cost += prices[left]
            left += 1
            right -= k

        # Maximum cost: buy most expensive, take k cheapest free
        max_cost = 0
        left, right = 0, n - 1
        while left <= right:
            max_cost += prices[right]
            right -= 1
            left += k

        return [min_cost, max_cost]
