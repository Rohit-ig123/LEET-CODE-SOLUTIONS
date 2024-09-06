class Solution {
public:
    int strStr(string haystack, string needle) {
        int i=0,j=0;
        int count=0;
        int index=0;
        if (haystack.length()>=needle.length())
        {
        for (i=0;i<=(haystack.length()-needle.length());i++)
        {
            if (haystack[i]==needle[0])
            {
                index=i;
                for (j=0;j<needle.length();j++)
                {
                if (haystack[i]==needle[j]){
                    count++;
                    i++;
                }
                    else
                    {
                        count=0;
                        i=index;
                        break;
                    }
                
                    
                }
                if (count==needle.length())
                {
                    break;
                }
                
            }
            
        }
          if (count==needle.length()){
        return index;}
        else
        { return -1;
        }
        
    }
        else 
        {   return -1;
        }
    }
};