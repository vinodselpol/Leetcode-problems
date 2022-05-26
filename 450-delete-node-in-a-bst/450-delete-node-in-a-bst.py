# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        
        if not root:
            return None
        
        
        if key< root.val:
            
            root.left= self.deleteNode(root.left, key)
        elif key > root.val:
            root.right= self.deleteNode(root.right, key)
            
            
        else :
            
            
            if (not root.left) or (not root.right):
                root= root.left if root.left else root.right
                
                
                
            else:
                
                cur=root.right
                
                
                while cur.left:
                    cur = cur.left

                root.val = cur.val
                root.right = self.deleteNode( root.right, cur.val )
                
                
        return root
                
                
                
                
            
            
        
        
        
       
        