class Solution:
    def maxArea(self, height: List[int]) -> int:
        area=0
        j=len(height)-1
        i=0
        while(i<j):
            area1=min(height[i],height[j])*(j-i)
            if (area1>area):
                area=area1
            if(height[i]<height[j]):
                i=i+1
            else:
                j=j-1
        return area
                
        


        