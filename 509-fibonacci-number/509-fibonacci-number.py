class Solution(object):
    def fib(self, n):
        
        if n==1:
            return 1
        if n==0:
            return 0
        
        
        return self.fib(n-1)+ self.fib(n-2)
        
        