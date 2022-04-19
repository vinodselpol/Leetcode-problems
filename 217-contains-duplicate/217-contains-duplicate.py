class Solution(object):
    def containsDuplicate(self, nums):
        
        duplicates={}
        
        for num in nums:
             if num not in duplicates:
                    duplicates[num]=1
             else :
                duplicates[num]+=1
                
        for element in duplicates:
            if duplicates[element]!=1:
                return True
        return False