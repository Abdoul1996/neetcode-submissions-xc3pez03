class Solution:
    from collections import Counter
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0 
        chars = set()
        best = 0 

        for right in range(len(s)):
            
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            
            chars.add(s[right])
            best = max(best, right - left + 1)
        
        return best


        