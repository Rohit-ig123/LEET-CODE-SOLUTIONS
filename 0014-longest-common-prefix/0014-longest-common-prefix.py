class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""
        
        
        first_string = strs[0]
        
        
        for i in range(len(first_string)):
           
            for string in strs[1:]:
  
                if i >= len(string) or string[i] != first_string[i]:
                    return first_string[:i]
        
        
        return first_string