#
# @lc app=leetcode.cn id=3000 lang=python
#
# [3000] 对角线最长的矩形的面积
#

# @lc code=start
class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """
        max_len, max_sqr = 0, 0
        for i in dimensions:
            l = i[0]*i[0] + i[1]*i[1]
            s = i[0]*i[1]
            if l > max_len:
                max_len = l
                max_sqr = s
            elif l == max_len:
                max_sqr = max(max_sqr, s)
        return max_sqr
            
# @lc code=end

