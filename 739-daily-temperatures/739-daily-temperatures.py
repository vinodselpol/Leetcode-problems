class Solution(object):
    def dailyTemperatures(self, t):
        res=[0]* len(t)
        
        stack=[]
        
        for i in range(len(t)):
            
            while stack and t[i]> t[stack[-1]]:
                cur=stack.pop()
                
                res[cur]=i-cur
                
                
            stack.append(i)
            
        return res
       