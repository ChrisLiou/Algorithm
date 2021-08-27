class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        maxLen=0
        #Don't use usedChar={}
        usedChar=set()
        
        while r<len(s):
            if s[r] not in usedChar:
                usedChar.add(s[r])
                r+=1
                maxLen=max(len(usedChar),maxLen)
            else:
                usedChar.remove(s[l])
                l+=1
                
        return maxLen