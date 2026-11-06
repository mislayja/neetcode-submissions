class Node:
    def __init__(self):
        self.ends = False
        self.chars = {}

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # is this suggesting building a prefix tree based on board? 
        trie = Node()

        for word in words:
            temp_trie=trie
            for char in word:
                if char not in temp_trie.chars:
                    temp_trie.chars[char]=Node()
                temp_trie = temp_trie.chars[char]
            temp_trie.ends = True
        
        res = []


        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()
        
        def dfs(r, c, node, word):
            if (r<0 or c<0 or r>=ROWS or c>=COLS or
                (r,c) in visit or board[r][c] not in node.chars):
                return 
            visit.add((r,c))
            node = node.chars[board[r][c]]
            word+= board[r][c]
            if node.ends:
                res.add(word)
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)
            visit.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,trie,"")
        return list(res)
            
