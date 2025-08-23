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
        sin = numRows * 2 - 2
        l = len(s)
        res = ""
        for i in range(numRows):
            if i == 0 or i == numRows-1:
                for j in range(i, l, sin):
                    res += s[j]
            else:
                for j in range(i, l, sin):
                    res += s[j]
                    if j + sin - 2*i < l:
                        res += s[j + sin - 2*i]
        return res
# @lc code=end

