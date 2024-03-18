class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        arrows = 0
        points.sort()
        end = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] > end:
                arrows += 1
                end =  points[i][1]
            else:
                end = min(end, points[i][1])
        return arrows + 1