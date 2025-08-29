#
# @lc app=leetcode.cn id=12 lang=python
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ""
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        for i in range(len(val)):
            while num >= val[i]:
                num -= val[i]
                res += syms[i]
        return res
# @lc code=end

