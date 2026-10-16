# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None

        #swap the children using DFS
        tmp1 = root.right
        root.right = root.left
        root.left = tmp1

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

        # queue = deque([root])
        # while queue:
        #     node = queue.popleft()
        #     node.right, node.left = node.left, node.right
        #     if node.right:
        #         queue.append(node.right)
        #     if node.left:
        #         queue.append(node.left)

        # return root


        # stack = [root]

        # while stack:
        #     node = stack.pop()
        #     node.left, node.right = node.right, node.left
        #     if node.right:
        #         stack.append(node.right)
        #     if node.left:
        #         stack.append(node.left)

        # return root



        