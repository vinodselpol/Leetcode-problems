class Solution(object):
    def construct2DArray(self, original, m, n):
        arr=[]
        
        if len(original)==m*n:
            for i in range(0, len(original),n):
                arr.append(original[i:i+n])
            return arr
       