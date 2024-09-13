class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.rstrip()
        count=0
        index=0
        
        for i in range(len(s)):
                if (s[i]==" "):
                        count=count+1
                        index=i
        if (count>0):
            value=len(s)-1-index
            return value
        else:
            return len(s.strip())
                
        