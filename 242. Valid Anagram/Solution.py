class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        d={}
        for c in s:
            if c in d:
                d[c]+=1
            else:
                d[c]=1
        for c in t:
            if c in d:
                d[c]-=1
            else:
                return False
            if d[c]<0:
                return False
        return True