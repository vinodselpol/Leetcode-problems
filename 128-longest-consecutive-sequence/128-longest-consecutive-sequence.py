class Solution(object):
    def longestConsecutive(self, nums):
        
        if not nums:
            return 0
        
        nums.sort()
        currentSequence=1
        maxSequence=0
        
        for i in range(1, len(nums)):
            
            if nums[i]== nums[i-1]:
                continue
            if nums[i]== nums[i-1] + 1:
                currentSequence+=1
                
            else :
                maxSequence=max(currentSequence, maxSequence)
                currentSequence=1
                
        
        return max(maxSequence, currentSequence)
                
                
            