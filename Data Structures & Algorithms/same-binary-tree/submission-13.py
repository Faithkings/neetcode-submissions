# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True
        if not p and q:
            return False
        if p and not q:
            return False

        stackp = [p]
        stackq = [q]

        while stackp and stackq:
            nodep = stackp.pop()
            nodeq = stackq.pop()
            if nodep.val != nodeq.val:
                return False
            if not nodep.right and nodeq.right:
                return False
            if not nodep.left and nodeq.left:
                return False
            if not nodeq.left and nodep.left:
                return False
            if not nodeq.right and nodep.right:
                return False
            if nodep.right and nodeq.right:
                stackp.append(nodep.right)
                stackq.append(nodeq.right)
            if nodep.left and nodeq.left:
                stackp.append(nodep.left)
                stackq.append(nodeq.left)   
        return True