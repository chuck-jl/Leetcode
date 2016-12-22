class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num ==1:
            return True
        if num <=0:
            return False
        count = 0
        while num>1:
            com=count
            if num%2==0:
                num/=2
                count+=1
            else:
                num= num
            if num%3==0:
                num/=3
                count+=1
            else:
                num = num
            if num%5==0:
                num/=5
                count+=1
            else:
                num=num
            if com== count:
                return False
            if num==1:
                return True