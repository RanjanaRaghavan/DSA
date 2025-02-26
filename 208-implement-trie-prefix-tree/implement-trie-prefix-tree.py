class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.isword = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur_node = self.root
        for w in word:
            pos = ord(w) - ord('a') 
            if not cur_node.children[pos]:
                cur_node.children[pos] = TrieNode() 
            cur_node = cur_node.children[pos]
        cur_node.isword = True
        

    def search(self, word: str) -> bool:
        cur_node = self.root
        for w in word:
            pos = ord(w) - ord('a')
            if not cur_node.children[pos]:
                return False
            
            cur_node = cur_node.children[pos]
        
        return cur_node.isword

            
        

    def startsWith(self, prefix: str) -> bool:
        cur_node = self.root
        for p in prefix:
            pos = ord(p) - ord('a')
            if not cur_node.children[pos]:
                return False
            
            cur_node = cur_node.children[pos]
        
        return True
            
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)