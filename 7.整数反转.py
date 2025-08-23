#
# @lc app=leetcode.cn id=7 lang=python
#
# [7] 整数反转
#

# @lc code=start
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MIN, INT_MAX = -2**31, 2**31-1
        res, dig = 0, 0
        
        while x != 0:
            dig = x % 10
            # Check for overflow before multiplying by 10
            if res > INT_MAX // 10 or res < INT_MIN // 10 + 1:
                return 0
            dig = dig-10 if x < 0 and dig > 0 else dig
            res = 10 * res + dig
            x = (x-dig) // 10
        return res 
# @lc code=end

