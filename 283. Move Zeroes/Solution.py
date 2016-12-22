class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        indexes=[i for i in xrange(len(nums)) if nums[i]==0]
        for i in reversed(indexes):
            del nums[i]
            nums.append(0)