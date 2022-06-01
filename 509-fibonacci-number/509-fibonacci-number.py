class Solution(object):
    def fib(self, n):
        
        
        if n <2:
            return n
        
        
        a, b=0,1
        
        for _ in range(2, n+1):
            c=a+b
            a=b
            b=c
            
            
            
        return c
    
        
       
        
        