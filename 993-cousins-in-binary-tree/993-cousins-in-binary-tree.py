# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        
        res=[]
        
        queue=deque([(root, None, 0)])
        
        
        while queue:
            
            if len(res)==2:
                break
                
            
            node, parent, depth=queue.popleft()
            
            
            if node.val ==x or node.val ==y:
                res.append((parent, depth))
                
                
            if node.left:
                queue.append((node.left, node, depth + 1))
                
                
            if node.right:
                queue.append((node.right, node, depth + 1))
                
                
        x, y= res
        
        return x[0]!= y[0] and x[1]==y[1]
        
    
            
            
            
            
        
        