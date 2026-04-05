class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Input : Adj List (Nodes to list) ==> Nei list 
        # output: 
        if not node:
            return None

        oldNew = {} # hashMap 

        def dfs(node):
            if node in oldNew:
                return oldNew[node]
            
            copy = Node(node.val)
            oldNew[node] = copy 
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy 
        return dfs(node)