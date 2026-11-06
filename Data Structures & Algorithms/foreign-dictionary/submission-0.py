class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # is this just creating a graph of comes before... comes after?
        # create adjacentcy list and then perform dfs until we have all characters in the list
        adj = {c:set() for w in words for c in w}
        for i in range(len(words)-1):
            w1,w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if w1[:minLen] == w2[:minLen] and len(w1)>len(w2): return ""

            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        visit = {} # false=visited, tru=current path
        res=[]
        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c]=True

            for nei in adj[c]:
                if dfs(nei): return True
            visit[c]=False
            res.append(c)
        # if dfs returns true, we detected a loop
        for c in adj:
            if dfs(c): return ""

        return "".join(reversed(res))
        # looking at word vs word