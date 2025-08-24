#
# @lc app=leetcode.cn id=1277 lang=python
#
# [1277] 统计全为 1 的正方形子矩阵
#

# @lc code=start
class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        row, col = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1
        return sum(sum(row) for row in dp)
# @lc code=end

