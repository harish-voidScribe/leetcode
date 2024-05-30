class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = Counter(nums)
        
        for x in hashmap:
            if hashmap[x] == 1:
                return x
            
        