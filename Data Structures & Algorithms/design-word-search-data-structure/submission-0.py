class Node:
    def __init__(self) -> None:
        self.ends = False
        self.chars = {}


class WordDictionary:
    def __init__(self):
        self.trie = Node()

    def addWord(self, word: str) -> None:
        node = self.trie
        for char in word:
            if char not in node.chars:
                node.chars[char] = Node()
            node = node.chars[char]
        node.ends = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            for j in range(i, len(word)):
                c = word[j]
                if c == ".":
                    return any(dfs(child, j + 1) for child in node.chars.values())
                if c not in node.chars:
                    return False
                node = node.chars[c]
            return node.ends

        return dfs(self.trie, 0)