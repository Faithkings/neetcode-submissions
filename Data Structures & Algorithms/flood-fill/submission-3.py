from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # original = image[sr][sc]
        # visited = set((sr,sc))
        # direction = [[-1,0], [0,-1], [1,0], [0,1]]
        # queue = deque([(sr,sc)])
        # image[sr][sc] = color

        # while queue:
        #     r, c = queue.popleft()
        #     for y, x in direction:
        #         xd = c + x
        #         yd = r + y
        #         if xd >= 0 and xd < len(image[0]) and yd >= 0 and yd < len(image) and (yd, xd) not in visited and image[yd][xd] == original:
        #             queue.append((yd, xd))
        #             image[yd][xd] = color  
        #             visited.add((yd, xd))
        # return image

        original = image[sr][sc]

        if original == color:
            return image

        def dfs(y, x):
            if y < 0 or y >= len(image) or x < 0 or x >= len(image[0]):
                return
            if image[y][x] != original:
                return 
            image[y][x] = color

            dfs(y + 1, x)
            dfs(y - 1, x)
            dfs(y, x + 1)
            dfs(y, x - 1)
        dfs(sr, sc)
        return image