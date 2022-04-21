class Solution(object):
    def findDuplicates(self, nums):
        output=[]
        
        for num in nums:
            num=abs(num)
            
            if nums[num-1]<0:
                output.append(num)
            else:
                nums[num-1]=-nums[num-1]
        return output
        