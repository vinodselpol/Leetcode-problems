class Solution(object):
    def maxArea(self, height):
        
        maxArea=0
        
        
        left=0
        right=len(height)-1
        
        
        while left < right:
            
            width=right-left
            
            minHeight=min(height[left], height[right])
            
            currentArea= width* minHeight
            
            maxArea=max(currentArea, maxArea)
            
            
            if height[left] < height[right]:
                left+=1
                
            else:
                right-=1
                
        return maxArea
            
            
            
            
            
            
            
        
        