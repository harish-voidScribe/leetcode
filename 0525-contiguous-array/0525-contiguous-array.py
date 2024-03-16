class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefixes = {0: -1}
        res = 0
        total = 0
        for i, v in enumerate(nums):
            total += 1 if v == 1 else -1
            if total in prefixes:
                res = max(res, i - prefixes[total])
            else:
                prefixes[total] = i
        return res