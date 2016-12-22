class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits)==0:
            return digits
        digits = digits[::-1]
        temp = 0
        carry = 1
        n = len(digits)
        i=0
        res=[]
        while i<n or carry >0:
            temp = 0
            if i<n:
                temp+=digits[i]
            if carry > 0:
                temp+= carry
            digit = temp%10
            carry = temp/10
            res.append(digit)
            i+=1
        return res[::-1]