class Solution(object):
    def change(self, amount, coins):
        
        
        dp=[0]*(amount+1)
        
        dp[0]=1
        
        for coin in coins:
            for j in range(1, amount+1):
                
                if j >= coin:
                    dp[j]+= dp[j- coin]
                    
        return dp[amount]
        
        