class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == " "or s== None:
            return 0
        temp = s.split()
        if temp ==[]:
            return 0
        res = temp[::-1]
        return len(res[0])