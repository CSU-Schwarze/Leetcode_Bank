#
# @lc app=leetcode.cn id=3021 lang=python
#
# [3021] Alice 和 Bob 玩鲜花游戏
#

# @lc code=start
class Solution(object):
    def flowerGame(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        if n < m:
            return self.flowerGame(m, n)
        num_min, num_max = 2, n+m
        res = 0
        for i in range(3, num_max+1, 2):
            if i-n <= 0:
                res += min(i-1, m)
            else:
                res += max(m-i+n+1, 0)
        return res
# @lc code=end

