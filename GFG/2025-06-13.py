def minBananasPerHour(arr, k):
    def canFinish(s):
        hours_needed = 0
        for bananas in arr:
            hours_needed += (bananas + s - 1) // s  
        return hours_needed <= k

    left, right = 1, max(arr)
    result = right

    while left <= right:
        mid = (left + right) // 2
        if canFinish(mid):
            result = mid 
            right = mid - 1
        else:
            left = mid + 1 

    return result
