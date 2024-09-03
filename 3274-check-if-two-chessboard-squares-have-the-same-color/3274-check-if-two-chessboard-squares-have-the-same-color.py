class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        col1,col2=coordinate1[0],coordinate2[0]
        row1,row2=int(coordinate1[1]),int(coordinate2[1])
        col1=ord(col1)-ord('a')+1
        col2=ord(col2)-ord('a')+1
        color1=(col1+row1)%2
        color2=(col2+row2)%2
        return color1==color2
            
        

            