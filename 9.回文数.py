#
# @lc app=leetcode.cn id=9 lang=python
#
# [9] 回文数
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            res, dig = 0, 0
            x1 = x
            while x > 0:
                dig = x % 10
                res = res * 10 + dig
                x //= 10
            if res == x1:
                return True
            else:
                return False
# @lc code=end

