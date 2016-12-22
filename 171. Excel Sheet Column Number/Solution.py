class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        index = dict(zip(list(string.uppercase), range(1,27)))
        time = 1
        result = 0
        for char in s[::-1]:
            result+=index[char]*time
            time*=26
        return result