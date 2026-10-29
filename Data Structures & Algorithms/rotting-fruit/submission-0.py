class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        row, column = len(grid), len(grid[0])
        queue = deque([])
        visited = set()
        time = 0
        for rw in range(len(grid)):
            for cn in range(len(grid[0])):
                if grid[rw][cn] == 2 and (rw, cn) not in visited:
                    queue.append((time, rw, cn))
                    visited.add((rw, cn))
        while queue:
            time, r, c = queue.popleft()
            for x, y in directions:
                if  0 <= r + x < row and 0 <= y + c < column and (r + x, c + y) not in visited and grid[r + x][c + y] == 1:
                    queue.append((time + 1, r + x, y + c))
                    visited.add((r + x, y + c))
                    grid[r + x][c + y] = 2  
        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1:
                    return -1
        return time            
            
        
        