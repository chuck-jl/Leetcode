class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums== [] :
            return 0
        if len(nums)== 1:
            return 1
        c=0
        for i,e in enumerate(nums[1:]):
            if e!=nums[c]:
                nums[c+1]= e
                c+=1
        return c+1