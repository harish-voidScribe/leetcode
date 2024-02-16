class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        if k == len(arr): return 0
        counts = sorted(Counter(arr).values())
        for i in range(len(counts)):
            if counts[i] <= k:
                k -= counts[i]
            else:
                return len(counts) - i
        return 0