# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        
        res=[]
        
        self.dfs(root, targetSum, res)
        
        return any(res)
    
    
    def dfs(self, root, target, res):
        
        #edge case
        if root :
            # edge case
            if not root.left and not root.right and root.val== target:
                res.append(True)
            
            
            
            if root.left:
                self.dfs(root.left, target-root.val, res)
                
            if root.right:
                self.dfs(root.right, target-root.val, res)
        
     