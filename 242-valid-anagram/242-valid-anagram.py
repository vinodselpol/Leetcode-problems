class Solution(object):
    def isAnagram(self, s, t):
        h={}
        sortedword="".join(sorted(s))
        
        if sortedword not in h:
            h[sortedword]=1
            
        sortedword1="".join(sorted(t))
        
        if sortedword1 not in h:
            return False
        
        return True