class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num/10:
            d=0
            while num >0:
                d+= num%10
                num/=10
            num = d
        return num
       