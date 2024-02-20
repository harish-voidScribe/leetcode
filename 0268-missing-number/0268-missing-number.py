class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = max(nums)
        for num in range(n + 1):
            if num not in nums:
                return num
        return n + 1