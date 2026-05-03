class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
       
        row_count = [0] * ROWS
        col_count = [0] * COLS
        

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    row_count[r] += 1
                    col_count[c] += 1

        communicating_servers = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                   
                    if row_count[r] > 1 or col_count[c] > 1:
                        communicating_servers += 1
                        
        return communicating_servers