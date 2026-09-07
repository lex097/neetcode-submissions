class TrieNode:
    def __init__(self, char, isWord):
        self.char = char
        self.isWord = False
        self.childMap = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode(None, False)
        self.inTrie = False
    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch in curr.childMap:
                curr = curr.childMap[ch]
            else:
                curr.childMap[ch] = TrieNode(ch, False)
                curr = curr.childMap[ch]
        curr.isWord = True

    def search(self, word: str) -> bool:
        self.inTrie = False
        self.dfs(self.root, word)
        return self.inTrie
    def dfs(self, node, word):
        if (word == ""):
            if node.isWord:
                self.inTrie = True
            return
        if (word[0] == "."):
            for n in node.childMap.keys():
                self.dfs(node.childMap[n], word[1:])
        elif (word[0] in node.childMap):
            self.dfs(node.childMap[word[0]], word[1:])
        