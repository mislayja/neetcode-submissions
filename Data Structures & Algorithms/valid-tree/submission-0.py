from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # we need to check whether there is a cylce, and that's it? 
        if not n: return True

        d = defaultdict(list)
        # we must create the adjacency list here
        for n1, n2 in edges:
            d[n1].append(n2)
            d[n2].append(n1)

        seen = set()
        

        def dfs(node, prev):
            if node in seen: return False
            seen.add(node)

            for neighbor in d[node]:
                if neighbor != prev:
                    if not dfs(neighbor, node): return False
            return True

        if not dfs(edges[0][0], -1): return False


        if len(seen) == n:
            return True
        return False

        # ok we need to iterate across this here


        # ok we must consider the case when not all nodes are connected