class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        val = len(nums)
        nums.sort()
        
        
        if nums[-1] == val:
           
            for i in range(len(nums) - 1, -1, -1):
                if nums[i] == val:
                    val -= 1
                else:
                    return val
        else:
           
            return val
        
        return val
