class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        bricks_used = 0
        increasing_paths = 0
        for i in range(1, len(heights)):
            difference = heights[i] - heights[i - 1]
            if difference <= 0:
                continue
            increasing_paths += 1 
            heappush(heap, -difference)
            bricks_used += difference
            while bricks_used > bricks:
                bricks_used += heappop(heap)
            if len(heap) + ladders < increasing_paths:
                return i - 1
        return len(heights) - 1