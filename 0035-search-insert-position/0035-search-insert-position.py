class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        for i in range(len(nums)):
                if (target<nums[0]):
                    return 0
                elif (target>nums[len(nums)-1]):
                    return len(nums)
                elif (target==nums[i]):
                    return i
                elif(target>nums[i] and target<nums[i+1]):
                    return i+1
                        
                        
                
                        
       
        