class Solution:
    def splitArray(self, arr, k):
        def canSplit(maxSum):
            current_sum = 0
            count = 1
            for num in arr:
                if current_sum + num > maxSum:
                    count += 1
                    current_sum = num
                    if count > k:
                        return False
                else:
                    current_sum += num
            return True

        left = max(arr)
        right = sum(arr)

        while left < right:
            mid = (left + right) // 2
            if canSplit(mid):
                right = mid
            else:
                left = mid + 1

        return left
