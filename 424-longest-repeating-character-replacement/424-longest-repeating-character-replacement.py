class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        frequency = {}
        longestLen = 0
        for r in range(len(s)):
            
            if  s[r] not in frequency:
                frequency[s[r]] = 0
            frequency[s[r]] += 1
            
            # Replacements cost = cells count between left and right - highest frequency
            cells_count = r - l + 1
            if cells_count - max(frequency.values()) <= k:
                longestLen = max(longestLen, cells_count)
                
            else:
                frequency[s[l]] -= 1
                # if not frequency[s[l]]:
                #     frequency.pop(s[l])
                l += 1
        
        return longestLen