class Solution:
    def getLucky(self, s: str, k: int) -> int:
        value=""
        result=0
        val=0
        for i in range(len(s)):
            val=ord(s[i])-ord('a')+1
            value=value+str(val)
        for k in range(k):
            result=0
            for i in range(len(value)):
                result=result+int(value[i])
            value=str(result)
           
        return result