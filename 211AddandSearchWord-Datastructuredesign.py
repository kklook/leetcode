# 写完这个题发现前面写的那个树有好多问题。
# 劣质网文害人啊！
class TrieNode(object):
    
    def __init__(self):
        self.childNodes = {}
        self.freq = 0
        
        
class WordDictionary(object):
    
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word):
        node = self.root
        pr = node
        count = 1
        for i in word:
            child = node.childNodes.get(i)
            if child == None:
                child = TrieNode()
                node.childNodes[i] = child
            node = child
        node.freq += 1

    def search(self, word):
        
        def find(node, word):
            if len(word) == 0:
                return node.freq > 0
            if word[0] == '.':
                for i in node.childNodes:
                    if find(node.childNodes[i], word[1:]):
                        return True
                return False
            else:
                if word[0] in node.childNodes:
                    node = node.childNodes[word[0]]
                    return find(node, word[1:])
                else:
                    return False
        
        return find(self.root, word)