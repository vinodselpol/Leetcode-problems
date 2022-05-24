# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        
        
        if not root:
            return 0
        
        
        res=[]
        queue=deque([(root, 1)])
        
        
        while queue:
            
            node, depth= queue.popleft()
            
            
            if not node.left and not node.right:
                res.append(depth)
                
                
                
            if node.left:
                queue.append((node.left, depth + 1))
                
                
            if node.right:
                queue.append((node.right, depth + 1))
                
        return res[-1]
       
        