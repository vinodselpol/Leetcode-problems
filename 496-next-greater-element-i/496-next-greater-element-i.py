class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        
        hashtable={}
        res=[]
        stack=[]
        
        
        for i in range(len(nums2)):
            
            
            while stack and nums2[i] > stack[-1]:
                hashtable[stack[-1]]= nums2[i]
                
                stack.pop()
                
            stack.append(nums2[i])
            
            
        for element in stack:
            hashtable[element]= -1
            
        for i in range(len(nums1)):
            
            res.append(hashtable[nums1[i]])
            
        return res
        

                
                
            
                
            
            
        
        