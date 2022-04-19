class Solution(object):
    def missingNumber(self, nums):
        hashtable={}
        
        for i in range(len(nums)+1):
            
            hashtable[i]=1
            
            
            
        for num in nums:
            if num in hashtable:
                hashtable[num]-=1
                
        for element in hashtable:
            if hashtable[element]==1:
                return element
            
            
            
        