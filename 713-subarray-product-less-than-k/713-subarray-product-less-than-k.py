class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        left=0
        res=0
        product=1
        
        for right in range(len(nums)):
            product*=nums[right]
            
            
            if product >= k:
                while product >=k and left <=right:
                    product/=nums[left]
                    left+=1
            
            
            
            
            res+=right-left + 1
            
        return res
                
                