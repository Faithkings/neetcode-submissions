# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # if not root:
        #     return 0

        # stack = [[root, 1]]
        # res = 0

        # while stack:
        #     node, index = stack.pop()
        #     res = max(index, res)
        #     if node.left:
        #         stack.append([node.left, index + 1])
        #     if node.right:
        #         stack.append([node.right, index + 1])
        # return res

        if not root:
            return 0

        queue = deque([root])
        height = 0
        while queue:
            q = len(queue)
            for i in range(q):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            height += 1
        return height
        
                
                

            



