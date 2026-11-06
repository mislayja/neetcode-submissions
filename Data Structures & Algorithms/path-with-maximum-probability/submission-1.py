from collections import defaultdict

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        lowest = 0

        d = defaultdict(list)
        probs = dict()
        for idx, (e1,e2) in enumerate(edges):
            d[e1].append(e2)
            d[e2].append(e1)
            probs[(e1,e2)] = succProb[idx]
            probs[(e2,e1)] = succProb[idx]

        


        def dfs(node,parent, seen, prob):
            
            if node == end_node: 
                nonlocal lowest
                lowest=max(lowest,prob)
                return
            
            if node in seen: return
            seen.add(node)
            # we need to add probs as we iterate on node
            for neighbor in d[node]:
                if neighbor is not parent:
                    # we can calc prob here, and recurse
                    new_prob = prob*probs[(node,neighbor)]
                    dfs(neighbor,node,seen, new_prob)
            seen.remove(node)





        # ok we must start at start_node
        dfs(start_node,-1,set(),1) # start with 1.0 prob



        return lowest