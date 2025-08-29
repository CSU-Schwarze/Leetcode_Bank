class Solution(object):
    def maxValue(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0 for _ in range(len(nums))]
        left_max, right_min = [0 for _ in range(len(nums))], [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            if i == 0:
                left_max[i] = nums[i]
            else:
                left_max[i] = max(left_max[i-1], nums[i])
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                right_min[i] = nums[i]
            else:
                right_min[i] = min(right_min[i+1], nums[i])
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                res[i] = left_max[i]
            else:
                if left_max[i] > right_min[i+1]:
                    res[i] = res[i+1]
                else:
                    res[i] = left_max[i]
        return res