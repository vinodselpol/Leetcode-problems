class Solution(object):
    def findDisappearedNumbers(self, nums):
        hashtable={}
        arr=[]
        
        for i in range(1,len(nums)+1):
            if i not in hashtable:
                hashtable[i]=1
                
        for num in nums:
            if num in hashtable:
                hashtable[num]-=1
                
                
        for num in hashtable:
            if hashtable[num]==1:
                arr.append(num)
                
        return arr