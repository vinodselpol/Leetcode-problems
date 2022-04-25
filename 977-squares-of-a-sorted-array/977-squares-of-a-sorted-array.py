class Solution(object):
    def sortedSquares(self, nums):
        output=[0] * len(nums)
        
        left=0
        right=len(nums)-1
        
        for i in range(len(nums)-1, -1, -1):
            
            val1= abs(nums[left])
            val2= abs(nums[right])
            
            if val1 < val2:
                output[i]= val2*val2
                right-=1
                
            else:
                output[i]=val1*val1
                left+=1
        return output
        