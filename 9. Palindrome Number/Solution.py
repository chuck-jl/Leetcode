class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x< 0:
            return False
        num_digit = 0
        y = x
        while y!=0:
            y/=10
            num_digit+=1
        if num_digit == 1:
            return True
        a = 0
        t = 0
        while a< (num_digit/2):
            t = t*10 + x%10
            x/=10
            a+=1
        if num_digit%2==1:
            x/=10
        if x==t:
            return True
        else:
            return False