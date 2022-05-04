class Solution(object):
    def dailyTemperatures(self, temperatures):
        res=[0]* len(temperatures)
        
        stack=[]
        
        
        for i in range(len(temperatures)):
            
            while stack and temperatures[i] > temperatures[stack[-1]]:
                
                cur=stack.pop()
                
                res[cur]= i-cur
                
            stack.append(i)
            
        return res
        
        