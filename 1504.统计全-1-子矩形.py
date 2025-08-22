#
# @lc app=leetcode.cn id=1504 lang=python
#
# [1504] 统计全 1 子矩形
#

# @lc code=start
class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        cnt = 0
        row, col = len(mat), len(mat[0])
        # 计算每一行的连续1的数量
        for i in range(row):
            for j in range(1, col):
                if mat[i][j] == 1:
                    mat[i][j] += mat[i][j - 1]
        # 遍历每一行
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    continue
                width = mat[i][j]
                # 从当前行向上遍历，计算以当前点为右下角的全1子矩形数量
                for k in range(i, -1, -1):
                    width = min(width, mat[k][j])
                    if width == 0:
                        break
                    cnt += width
        return cnt
        
        
# @lc code=end

