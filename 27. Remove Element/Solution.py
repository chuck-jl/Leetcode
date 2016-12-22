class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for i,e in enumerate(nums):
            if e != val:
                nums[count] = nums[i]
                count+=1
        return count