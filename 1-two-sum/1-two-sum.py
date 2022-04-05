class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
      
        seen={}
        for i in range(len(nums)):
            match=target-nums[i]
            if match in seen:
                return [seen[match], i]
            seen[nums[i]]=i