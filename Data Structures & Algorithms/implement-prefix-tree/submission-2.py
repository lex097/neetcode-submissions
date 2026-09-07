class TrieNode:
    # char is the nodes corresponding character, children is it's connected nodes, isWord is whether it was inserted or not
    #self.children is a map with a char corresponding to its node
    def __init__(self, char, isWord):
        self.char = char
        self.children = {}
        self.isWord = isWord


class PrefixTree:

    def __init__(self):
        self.root = TrieNode(None, False)
    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch in curr.children:
                curr = curr.children[ch]
            else:
                curr.children[ch] = TrieNode(ch, False)
                curr = curr.children[ch]
        curr.isWord = True
    def search(self, word: str) -> bool:
        curr = self.root
        for i in range(0, len(word)):
            if (word[i] not in curr.children):
                return False
            curr = curr.children[word[i]]
        if curr.isWord:
            return True
        return False
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in range(0, len(prefix)):
            if (prefix[i] not in curr.children):
                return False
            curr = curr.children[prefix[i]]
        return True
        
        