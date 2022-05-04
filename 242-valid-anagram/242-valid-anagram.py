class Solution(object):
    def isAnagram(self, s, t):
        h={}
        
        
        for letter in s:
            if letter not in h:
                h[letter]=1
                
            else:
                h[letter]+=1
                
                
        for letter in t:
            if letter in h:
                h[letter]-=1
                
            else:
                h[letter]=1
                
                
                
                
        for value in h.values():
            if value !=0:
                return False
        return True
        