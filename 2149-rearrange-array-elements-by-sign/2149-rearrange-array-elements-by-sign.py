class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        pos, neg = 0, 1
        for num in nums:
            if num < 0:
                res[neg] = num
                neg += 2
            else:
                res[pos] = num
                pos += 2
        return res