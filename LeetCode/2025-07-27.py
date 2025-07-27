class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        # Step 1: Remove consecutive duplicates
        compressed = [nums[0]]
        for num in nums[1:]:
            if num != compressed[-1]:
                compressed.append(num)

        # Step 2: Count hills and valleys
        count = 0
        for i in range(1, len(compressed) - 1):
            if compressed[i] > compressed[i - 1] and compressed[i] > compressed[i + 1]:
                count += 1  # Hill
            elif compressed[i] < compressed[i - 1] and compressed[i] < compressed[i + 1]:
                count += 1  # Valley

        return count
