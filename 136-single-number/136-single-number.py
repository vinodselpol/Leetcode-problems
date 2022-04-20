class Solution(object):
    def singleNumber(self, nums):
        hashtable={}
        
        for num in nums:
            if num not in hashtable:
                hashtable[num]=1
            else:
                hashtable[num]+=1
                
        for num in hashtable:
            if hashtable[num]==1:
                return num
        