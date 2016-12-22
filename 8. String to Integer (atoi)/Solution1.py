class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str) == 0:
            return 0
            
        # remove spaces in the front and decide if negative 
        while str[0] == ' ':
            str = str[1:]
            
        if str[0]  == '-':
            neg = True
            str = str[1:]
        elif str[0]  == '+':
            neg = False
            str = str[1:]
        else: neg = False
        
        # convert into integer
        valid = ['0','1','2','3','4','5','6','7','8','9']
        result = 0
        for i in range(len(str)):
            if str[i] in valid:
                result = 10*result + int(str[i])
            else:
                break
            
        # deal with overflow
        if result > 2**31-1:
            if neg: return -2**31
            else: return 2**31 - 1
        else:
            if neg: return -result
            else: return result 