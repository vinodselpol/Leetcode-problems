class Solution(object):
    def productExceptSelf(self, nums):
        
        product=1
        output=[]
        
        for i in range(len(nums)):
            output.append(product)
            product=product*nums[i]
            
        product=1
        
        for i in range(len(nums)-1, -1, -1):
            output[i]=output[i]*product
            product=product*nums[i]
        return output
            
        
        
        