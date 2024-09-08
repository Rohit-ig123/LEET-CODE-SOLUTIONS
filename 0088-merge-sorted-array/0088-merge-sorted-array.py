class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        for j in range(n):
                nums1[m]=nums2[j]
                m=m+1
        nums1.sort()
        
                
        
                
                                
        
        