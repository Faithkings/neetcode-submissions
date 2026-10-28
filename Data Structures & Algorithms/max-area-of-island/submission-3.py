class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        def dfs(x, y):
            if (x, y) in visited:
                return
            if x < 0 or x > len(grid) - 1 or y < 0 or y > len(grid[0]) - 1 or grid[x][y] == 0:
                return
            visited.add((x, y))
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        max_count = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 1 and (row,column) not in visited:
                    before = len(visited)
                    dfs(row, column)
                    count = len(visited) - before
                    max_count = max(max_count, count)
        return max_count
        