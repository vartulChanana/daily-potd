class Solution:
    def printKClosest(self, arr, k, x):
        if x in arr:
            arr.remove(x)
        
        arr.sort(key=lambda a: (abs(a - x), -a))
        
        return arr[:k]

