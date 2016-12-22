class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 :
           return s
        else:
           
           step = 2*numRows -2
           result = s[::step]
           for i in range(1, numRows-1):
               for j in range(i, len(s), step):
                  result+=s[j]
                  if j+(step -i*2)<len(s):
                      result+=s[j+(step -i*2)]
                  
           result += s[numRows-1::step]
           return result