#
# @lc app=leetcode.cn id=11 lang=python
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        l, r = 0, len(height)-1
        while l < r:
            area = min(height[l], height[r]) * (r-l)
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
                while height[l] <= height[l-1] and l < r:
                    l += 1 
            else:
                r -= 1 
                while height[r] <= height[r+1] and l < r:
                    r -= 1 
        return res
# @lc code=end

