class Solution(object):
    
    def cloneGraph(self, node):
        if not hasattr(node, 'label'):
            return None
        nodeDict = {}
        nodeStack = []
        newNode = UndirectedGraphNode(node.label)
        nodeDict[node.label] = newNode
        nodeStack = [node]
        while nodeStack:
            top = nodeStack.pop()
            temp = nodeDict[top.label]
            for i in top.neighbors:
                if not i.label in nodeDict:
                    nodeDict[i.label] = UndirectedGraphNode(i.label)
                    nodeStack.append(i)
                temp.neighbors.append(nodeDict[i.label])
        return newNode