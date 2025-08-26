#
# @lc app=leetcode.cn id=8 lang=python
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        isNegative, hasNum, hasNP = True, False, False
        res = 0
        for i in s:
            if i == ' ':
                if hasNum or hasNP:
                    break
                continue
            elif i == '-':
                if hasNum or hasNP:
                    break
                hasNP = True
                isNegative = False
            elif i == '+':
                if hasNum or hasNP:
                    break
                hasNP = True
                isNegative = True
            else:
                if i not in '0123456789':
                    break
                hasNum = True
                n = int(i)
                if isNegative:
                    if res > INT_MAX // 10 or (res == INT_MAX // 10 and n > INT_MAX % 10):
                        return INT_MAX
                else:
                    if res > -(INT_MIN // 10)-1 or (res == -(INT_MIN // 10)-1 and n > 10 - INT_MIN % 10):
                        return INT_MIN
                res = res * 10 + n
        return res if isNegative else -res
# @lc code=end

