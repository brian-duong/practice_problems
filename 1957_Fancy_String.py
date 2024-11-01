class Solution:
    def makeFancyString(self, s: str) -> str:
        ret = s[:2]
        for i in range(2, len(s)):
            if s[i] != s[i-1] or s[i] != s[i-2]:
                ret += s[i]
        return ret
        
