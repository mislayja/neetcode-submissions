from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # this is exactly same as last problem except we just keep going till count is equal...
        d = defaultdict(list)
        for n1,n2 in edges:
            d[n1].append(n2)
            d[n2].append(n1)
        
        seen = set()
        total = 0

        def dfs(node, prev):
            if node in seen: return False
            seen.add(node)
            for neighbor in d[node]:
                if neighbor != prev:
                    dfs(neighbor, node)
            return True
        
        for val in range(n):
            if dfs(val, -1): total+=1
        return total