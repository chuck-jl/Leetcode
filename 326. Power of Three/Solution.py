class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0 or n==2:
            return False
        if n==1:
            return True
        while n>0:
            if n%3==0:
                n/=3
                if n==1:
                    return True
            else:
                return False