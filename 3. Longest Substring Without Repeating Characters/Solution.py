class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        cur = 0
        d = {}
        for i, e in enumerate(s):
            if e not in d:
                cur = cur +1
            else:
                cur = min(i-d[e], cur+1)
            d[e]=i
            res = max(res, cur)
        return res