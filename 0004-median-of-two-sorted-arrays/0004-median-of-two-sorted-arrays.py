class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result=nums1+nums2
        result=sorted(result)
        median=None
        if (len(result)%2==1):
            val=(len(result)+1)//2
            median=result[val-1]
        else:
            val=(len(result)//2)
            median=(result[val-1]+result[val])/2
        return median


        