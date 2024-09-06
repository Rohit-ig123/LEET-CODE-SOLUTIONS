class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new=[]
        j=0
        
        for i in range(len(nums)):
            if ((val)!=(nums[i])):
                new.append(nums[i])
                
               
        for i in range (len(new)):
            nums[i]=new[j]
            j=j+1
        return(len(new))