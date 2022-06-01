class Solution(object):
    def tribonacci(self, n):
        
        if n <2:
            return n
        if n==2:
            return 1
        
        a,b,c=0,1,1
        
        for _ in range(3, n+1):
            d=a+b+c
            a=b
            b=c
            c=d
            
        return d
            
        
    
    
    
       
        