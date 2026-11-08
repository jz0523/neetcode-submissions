class TrieNode():
    def __init__(self):
        self.children = {}
        self.isLeaf = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isLeaf = True
        

    def search(self, word: str) -> bool:
        def dfs(i, cur):
            if i >= len(word):
                return cur.isLeaf

            c = word[i]
            if c == ".":
                for node in cur.children.values():
                    if dfs(i + 1, node):
                        return True
                return False
            else:
                if c not in cur.children:
                    return False
                return dfs(i + 1, cur.children[c])

        return dfs(0, self.root)
        

