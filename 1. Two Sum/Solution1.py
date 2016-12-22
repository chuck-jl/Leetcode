class Solution(object):
    def twoSum(self, nums, target):
        d ={}
        for i in range(len(nums)):
            e = nums[i]
            if e in d:
                return d[e], i
            d[target-e]= i