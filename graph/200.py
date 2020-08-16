# 200. Number of Islands

class Solution:
    def dfs(self, startx: int, starty: int):
        if self.grid[startx][starty] == '1':
            self.grid[startx][starty] = '0'
        else:
            return
        
        if startx - 1 >= 0:
            self.dfs(startx - 1, starty)
        if startx + 1 < len(self.grid):
            self.dfs(startx + 1, starty)
        if starty - 1 >= 0:
            self.dfs(startx, starty - 1)
        if starty + 1 < len(self.grid[0]):
            self.dfs(startx, starty + 1)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        self.grid = grid
        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                if self.grid[r][c] == '1':
                    cnt += 1
                    self.dfs(r, c)
                    
        return cnt
