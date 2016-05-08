# 跟我说 T~r~i~e Trie
class TrieNode(object):
    
    def __init__(self, word):
        self.childNodes = {}
        self.nodeValue = word
        self.freq = 0
        
        
class Trie(object):

    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word):
        node = self.root
        for i in word:
            child = node.childNodes.get(i)
            if child == None:
                child = TrieNode(i)
                node.childNodes[i] = child
            node = child
        node.freq += 1
    def search(self, word):
        node = self.root
        for i in word:
            if i in node.childNodes:
                node = node.childNodes[i]
            else:
                return False
        if node.freq > 0:
            return True
        else:
            return False
    
    def startsWith(self, prefix):
        node = self.root
        for i in prefix:
            if i in node.childNodes:
                node = node.childNodes[i]
            else:
                return False
        return True