class TrieNode:
    def __init__(self):
        self.end=False
        self.key={}
        
class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node=self.root
        for i in word:
            if i not in node.key:
                node.key[i]=TrieNode()
            node=node.key[i]
        node.end=True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node=self.root
        for i in word:
            if i not in node.key:
                return False
            node=node.key[i]
        return node.end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node=self.root
        for i in prefix:
            if i not in node.key:
                return False
            node=node.key[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)