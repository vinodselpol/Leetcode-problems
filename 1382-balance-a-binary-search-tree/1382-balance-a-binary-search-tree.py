# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        
        output=[]
        
        self.inOrder(root, output)
        
        return self.convert(output, 0, len(output))
        
        
    def convert(self, nums, left, right):
        
        if left==right:
            return None
        
        mid=(left+right)//2
        
        node=TreeNode(nums[mid])
        node.left=self.convert(nums, left, mid)
        node.right=self.convert(nums, mid+1, right)
        return node
        
        
        
    def inOrder(self, root, output):
        if not root:
            return None
        
        
        self.inOrder(root.left, output)
        output.append(root.val)
        self.inOrder(root.right, output)
        
        
        
        