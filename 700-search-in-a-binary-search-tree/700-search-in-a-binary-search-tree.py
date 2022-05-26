# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        
        
        queue=deque([root])
        
        while queue:
            node=queue.popleft()
            if node:
                if val==node.val:
                    return node
                
                if val < node.val:
                    queue.append(node.left)
                else:
                    queue.append(node.right)
                    
        return None
                
                
        
        
            
        
        
    
        
        
        
        