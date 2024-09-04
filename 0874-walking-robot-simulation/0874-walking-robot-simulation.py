class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ans = 0
        d = 0  
        x = 0  
        y = 0  
        obstaclesSet = {(ox, oy) for ox, oy in obstacles}

        for c in commands:
            if c == -1:  
                d = (d + 1) % 4
            elif c == -2: 
                d = (d + 3) % 4
            else:  # move forward
                for _ in range(c):
                    nx = x + dirs[d][0]
                    ny = y + dirs[d][1]
                    if (nx, ny) in obstaclesSet: 
                        break
                    x = nx
                    y = ny

            ans = max(ans, x * x + y * y)  # update the maximum distance

        return ans
