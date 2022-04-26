class Solution(object):
    def minSubArrayLen(self, target, nums):
        left=0
        
        sum=0
        output=len(nums)+1
        
        
        
        
        for right in range(len(nums)):
            sum+=nums[right]
            
           
            while sum >= target:
                output=min(output, right-left + 1)
                sum=sum-nums[left]
                left+=1
                
                
            
                
        return output if output <=len(nums) else 0
            
            