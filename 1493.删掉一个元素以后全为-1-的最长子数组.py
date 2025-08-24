#
# @lc app=leetcode.cn id=1493 lang=python
#
# [1493] 删掉一个元素以后全为 1 的最长子数组
#

# @lc code=start
class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        zero = -1
        left = 0
        max_len = 0
        for i, num in enumerate(nums):
            if num == 0:
                left = zero+1
                zero = i
            if i-left > max_len:
                max_len = i-left
        return max_len
# @lc code=end

