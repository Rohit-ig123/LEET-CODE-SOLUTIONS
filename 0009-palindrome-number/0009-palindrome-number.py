class Solution:
    def isPalindrome(self, x: int) -> bool:
        x1=str(x)
        if (x1[0:]==x1[::-1]):
            return True
        else:
            return False        