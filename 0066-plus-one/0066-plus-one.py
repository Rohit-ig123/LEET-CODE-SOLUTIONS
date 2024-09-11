class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=0
        
        if (len(digits)==1):
                        carry=(digits[0]+1)//10
                        if (carry>0):
                            val=(digits[0]+1)%10
                            digits.append(val)
                            digits[0]=carry
                            return digits
                        else:
                                digits[0]=digits[0]+1
                    
                                return digits
        else:
            digits[len(digits) - 1] += 1
            for i in range(len(digits) - 1, -1, -1):
                if digits[i] + carry > 9:
                    digits[i] = (digits[i] + carry) % 10
                    carry = 1
                else:
                    digits[i] += carry
                    carry = 0
            if carry == 1:
                digits.insert(0, 1)

        return digits