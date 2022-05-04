class Solution(object):
    def groupAnagrams(self, strs):
        
        hashtable={}
        
        for word in strs:
            sortedWord="".join(sorted(word))
            
            if sortedWord not in hashtable:
                
                hashtable[sortedWord]= [word]
                
            else:
                hashtable[sortedWord].append(word)
        output=[]
        
        for value in hashtable.values():
            
            output.append(value)
            
        return output
            
                
        
        