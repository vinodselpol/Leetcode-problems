# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        
        queue= deque([root])
        
        
        while queue:
            
            node= queue.popleft()
            
         
            if node is None:
                continue
                
            
            node.left, node.right= node.right, node.left
            
            if node.left:
                
                 queue.append(node.left)
                    
            if node.right:
                
                queue.append(node.right)
                
                
                
                
        return root
        
                
                

        
        
        
        
        
        