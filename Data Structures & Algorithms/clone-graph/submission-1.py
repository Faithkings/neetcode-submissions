"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oriclo = {}
        def dfs(node):
            if not node:
                return None
            if node in oriclo:
                return oriclo[node]

            clone = Node(node.val)
            oriclo[node] = clone
            
            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei))
            return clone   

        return dfs(node)    

        

            
        