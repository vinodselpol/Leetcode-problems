class Solution(object):
    def groupAnagrams(self, strs):
        
        h={}
        
        for word in strs:
            sortedword="".join(sorted(word))
            
            
            if sortedword not in h:
                h[sortedword]=[word]
                
            else:
                h[sortedword].append(word)
                
                
        return h.values()