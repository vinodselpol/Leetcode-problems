class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        hashtable={}
        count=0
        
        for i in range(len(stones)):
            if stones[i] not in hashtable:
                hashtable[stones[i]]=1
            else:
                hashtable[stones[i]]+=1
                
                
        for char in jewels:
            if char in hashtable:
                count+= hashtable[char]
                
                
        return count