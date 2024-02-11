class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dp = {(0, COLS - 1): grid[0][0] + grid[0][COLS - 1]}
        for row in range(1, ROWS):
            new_dp = defaultdict(int)
            for (bot1, bot2), val in dp.items():
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        nbot1, nbot2 = bot1 + i, bot2 + j
                        if 0 <= nbot1 < COLS and 0 <= nbot2 < COLS:
                            total = grid[row][nbot1] + (grid[row][nbot2] if nbot1 != nbot2 else 0)
                            new_dp[(nbot1, nbot2)] = max(new_dp[(nbot1, nbot2)], total + val)
            dp = new_dp
        return max(dp.values())
        