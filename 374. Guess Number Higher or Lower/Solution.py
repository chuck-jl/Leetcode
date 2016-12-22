# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=1
        e=n+1
        num=1
        while s<e:
            num=(s+e)>>1
            res=guess(num)
            if res==0:
                return num  

            elif res<0:
                e=num
            else:
                s=num+1
        return s
