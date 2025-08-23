#
# @lc app=leetcode.cn id=6 lang=python
#
# [6] Z 字形变换
#

# @lc code=start
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < 2:
            return s
        res = ["" for _ in range(numRows)]
        i, step = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows-1:
                step = -step
            i += step
        return "".join(res)
# @lc code=end

