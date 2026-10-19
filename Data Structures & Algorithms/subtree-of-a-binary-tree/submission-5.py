# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # if not root and not subRoot:
        #     return True
        # if not root and subRoot:
        #     return False
        # if not subRoot and root:
        #     return False
        
        # if root.left.val == subRoot.right.val and root.val == subRoot.val:
        #     return True
        
        # if root.val != subRoot.val:
        #     left = self.isSubtree(root.left, subRoot)
        #     right = self.isSubtree(root.right, subRoot)
        
        # if root.val == subRoot.val:
        #     left = self.isSubtree(root.left, subRoot.left)
        #     right = self.isSubtree(root.right, subRoot.right)

        # return left or right
        
        def sameTree(p, q):

            if not p and not q:
                return True
            if p and not q:
                return False
            if not p and q:
                return False
            
            if p.val != q.val:
                return False

            left = sameTree(p.left, q.left)
            right = sameTree(p.right, q.right)

            return left and right
        
        if not root and not subRoot:
            return True
        if root and not subRoot:
            return True
        if not root and subRoot:
            return False
        if sameTree(root, subRoot):
            return True
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right
        