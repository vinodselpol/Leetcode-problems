class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        hashtable={}
        count=0
        
        for char in stones:
            if char not in hashtable:
                hashtable[char]=1
            else:
                hashtable[char]+=1
                
                
        for char in jewels:
            if char in hashtable:
                count+= hashtable[char]
                
                
        return count