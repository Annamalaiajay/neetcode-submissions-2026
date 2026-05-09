class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if r == 0 and c == 0:
                    continue
                elif r == 0: 
                    grid[r][c] += grid[r][c - 1]
                elif c == 0: 
                    grid[r][c] += grid[r - 1][c]
                else: 
                    grid[r][c] += min(grid[r - 1][c], grid[r][c - 1])
        
        return grid[rows - 1][cols - 1]