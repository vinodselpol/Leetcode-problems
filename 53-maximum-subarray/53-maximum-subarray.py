class Solution(object):
    def maxSubArray(self, nums):
        
        
        currentSum=nums[0]
        maxSum=nums[0]
        
        for num in nums[1:]:
            currentSum=max(num, currentSum + num)
            maxSum=max(currentSum, maxSum)
            
        return maxSum
                
            
        
        
        
        