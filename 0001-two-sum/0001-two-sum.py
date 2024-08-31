class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       
        j=0
        value=[]
        for j in range(len(nums)-1):
            for i in range(j+1,len(nums)):
                if(nums[j]+nums[i]==target):
                    value=[j,i]
                    return value
                    break;
                
                