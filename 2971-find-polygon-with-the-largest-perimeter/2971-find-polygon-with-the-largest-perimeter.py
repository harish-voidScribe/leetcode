class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        res = -1
        total = sum(nums[:2])
        for i in range(2, len(nums)):
            if nums[i] < total:
                res = total + nums[i]
            total += nums[i]
        return res