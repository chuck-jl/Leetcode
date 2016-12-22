class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        d =[]
        while n not in d:
            d.append(n)
            t = n
            s = 0
            while t!=0:
                digit = t%10
                s+=digit*digit
                t/=10
            n=s
            if n==1:
                return True
        return False