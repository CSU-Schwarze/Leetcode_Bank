#
# @lc app=leetcode.cn id=16 lang=python
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        diff = float('inf')
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                if l > i+1 and nums[l] == nums[l-1]:
                    l += 1
                    continue
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return s
                elif s > target:
                    if abs(s-target) < abs(diff):
                        diff = s-target
                    r -= 1
                else:
                    if abs(s-target) < abs(diff):
                        diff = s-target
                    l += 1
        return target+diff
                        
        
# @lc code=end

