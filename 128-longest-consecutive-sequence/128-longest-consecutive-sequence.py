class Solution(object):
    def longestConsecutive(self, nums):
        
        if not nums:
            return 0
        
        
        nums.sort()
        
        current=1
        maximum=0
        
        
        for i in range(1, len(nums)):
            
            if nums[i]==nums[i-1]:
                continue
                
            if nums[i]==nums[i-1] + 1:
                current+=1
                
            else :
                maximum=max(maximum, current)
                current=1
                
        return max(maximum, current)
        
        
                
                
            