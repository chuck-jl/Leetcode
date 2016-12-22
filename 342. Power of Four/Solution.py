class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num ==1:
            return True
        if num<4:
            return False
        while num>0:
            if num%4==0:
                num/=4
            else:
                return False
            if num ==1:
                return True