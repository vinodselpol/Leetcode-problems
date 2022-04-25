class Solution(object):
    def backspaceCompare(self, S, T):
        
        i, j = len(S), len(T) # two indexes, start outside of string to make loop simpler
        
        while i >= 0 and j >= 0:
            back = 1 # backspace counter, move back at least one character
            while back > 0:
                i -= 1
                back += 1 if i >= 0 and S[i] == '#' else -1 # if hashtag found increase backspace counter, otherwise decrease it

            back = 1
            while back > 0:
                j -= 1
                back += 1 if j >= 0 and T[j] == '#' else -1
            
            if i >= 0 and j >= 0 and S[i] != T[j]: # done with backspaces, compare current character
                return False
        
        return i < 0 and j < 0 # return True if both indexes passed both strings fully
        