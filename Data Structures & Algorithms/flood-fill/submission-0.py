from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]
        visited = set()
        direction = [[-1,0], [0,-1], [1,0], [0,1]]

        queue = deque()
        queue.append((sr,sc))
        image[sr][sc] = color
        visited.add((sr,sc))

        while queue:
            r, c = queue.popleft()
            for y, x in direction:
                xd = c + x
                yd = r + y
                if xd >= 0 and xd < len(image[0]) and yd >= 0 and yd < len(image) and (yd, xd) not in visited and image[yd][xd] == original:
                    queue.append((yd, xd))
                    image[yd][xd] = color  
                visited.add((yd, xd))
        return image