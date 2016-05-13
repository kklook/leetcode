# TrieTree + dfs
class TrieNode(object):
    
    def __init__(self):
        self.child = {}
        self.isWord = False
        
        
class Trie(object):
    
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for i in word:
            if not i in node.child:
                node.child[i] = TrieNode()
            node = node.child[i]
        node.isWord = True
    
    def delete(self, word):
        node = self.root
        deleteList = []
        for i in word:
            if i in node.child:
                deleteList.append((i, node))
                node = node.child[i]
            else:
                return False
        if not node.isWord:
            return False
        if len(node.child):
            node.isWord = False
        else:
            for i, node in reversed(deleteList):
                del node.child[i]
                if len(node.child) or node.isWord:
                    break
           
                
class Solution(object):
    
    def findWords(self, board, words):
        w, h = len(board[0]), len(board)
        result = []
        dp = [[False] * w for i in range(h)]
        trieTree = Trie()
        for word in words:
            trieTree.insert(word)
            
        def dfs(x, y, node, word):
            node = node.child.get(board[x][y])
            if node == None:
                return None
            dp[x][y] = True
            for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dx, dy = x + i, y + j
                if dx >= 0 and dy >= 0 and dx < h and dy < w and not dp[dx][dy]:
                    dfs(dx, dy, node, word+board[dx][dy])
            if node.isWord:
                result.append(word)
                trieTree.delete(word)
            dp[x][y] = False
            
        for i in range(h):
            for j in range(w):
                if board[i][j] in trieTree.root.child:
                    dfs(i, j, trieTree.root, board[i][j])
        return result