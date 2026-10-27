class Solution:
    from collections import defaultdict
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        connections = defaultdict(list)

        for node, child in edges:
            connections[node].append(child)
            connections[child].append(node)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return
            else:
                visited.add(node)
            for neighbors in connections[node]:
                dfs(neighbors)

        dfs(0)
        if len(visited) - 1 == len(edges):
            return True
        else:
            return False



        

        

        