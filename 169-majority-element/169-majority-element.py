class Solution(object):
    def majorityElement(self, nums):
        elements={}
        
        for num in nums:
            if num not in elements:
                elements[num]=1
            else :
                elements[num]+=1
        
        maximum=0
        majorityElement=0
        for element in elements:
            if elements[element] > maximum:
                maximum = elements[element]
                majorityElement=element
        return majorityElement
                
        