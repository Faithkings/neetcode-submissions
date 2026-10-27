class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        def dfs(r, c):
            island = 0
            if r >= len(grid) or r < 0 or c >= len(grid[0]) or c < 0:
                return 
            if grid[r][c] == '0':
                return
            if (r, c) in visited:
                return
            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        island = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == '1' and (row, column) not in visited:
                    island += 1
                    dfs(row,column) 
        return island  

