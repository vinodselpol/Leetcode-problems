import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        
        freq={}
        ans=[]
        
        for num in nums:
            if num not in freq:
                freq[num]=1
                
            else:
                freq[num]+=1
                
                
        for key, val in freq.items():
            
            if len(ans) < k:
                heapq.heappush(ans, [val, key])
                
            else:
                heapq.heappushpop(ans, [ val, key])
                
        return [key for val, key in ans]
                
                
        
                
        
                
        
        