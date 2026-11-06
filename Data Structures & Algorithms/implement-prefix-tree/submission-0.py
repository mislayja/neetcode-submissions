class PrefixTree:
    class Node:
        def __init__(self):
            self.ends=False
            self.chars = dict()


    def __init__(self):
        self.chars = self.Node()

    def insert(self, word: str) -> None:
        chars = self.chars
        for char in word:
            if char not in chars.chars:
                chars.chars[char] = self.Node()
            chars = chars.chars[char]
        chars.ends=True

    def search(self, word: str) -> bool:
        trie = self.chars
        for char in word:
            if char in trie.chars:
                trie = trie.chars[char]
            else: return False
        return trie.ends
        
        

    def startsWith(self, prefix: str) -> bool:
        trie = self.chars
        for char in prefix:
            if char in trie.chars:
                trie = trie.chars[char]
            else: return False
        return True
        