class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result=[]
        length=0
        i=0
        while(i<len(s)):
            
            for j in range(i,len(s)):
                if (s[j] not in result):
                    result.append(s[j])
                else:
                    if(length<len(result)):
                        length=len(result)
                        result=[]
                        i=i+1
                        break
                    else:
                        result=[]
                        i=i+1
                        break
        return length            

                
        