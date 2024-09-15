from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:  
            return ""
        if len(strs)==1:
            return strs[0]
        
        val = strs[0] 
        string = ""  
        
       
        for i in range(min(len(val), len(strs[1]))):  
            if val[i] == strs[1][i]:  
                string += val[i]  
            else:
                break  
        
        if not string:  
            return ""
        
        
        for j in range(2, len(strs)):
            for k in range(len(string)):
                if k >= len(strs[j]) or strs[j][k] != string[k]:  
                    string = string[:k]  
                    break
        
        return string
