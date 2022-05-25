# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        parents, queue, visited = {}, collections.deque([(target, 0)]), set()
        self.getParents(root, None, parents)
        res = []
        while queue:
            node, dist = queue.popleft()   
            if node not in visited:
                if dist == k: res.append(node.val)
                visited.add(node)
                
                if node.left: queue.append((node.left, dist+1))
                if node.right: queue.append((node.right, dist+1))
                if parents[node]: queue.append((parents[node], dist+1))
        
        return res
        
        #function to get a pointer to parent node
    def getParents(self, root, parent, hmap):
        if not root:
            return 
        hmap[root] = parent
        if root.left: self.getParents(root.left, root, hmap)
        if root.right: self.getParents(root.right, root, hmap)   
        
   