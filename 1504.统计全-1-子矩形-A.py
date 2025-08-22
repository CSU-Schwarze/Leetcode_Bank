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
        heights = [0] * len(mat[0])
        cnt = 0
        
        for row in mat:
            for i, v in enumerate(row):
                heights[i] = heights[i] + 1 if v else 0
            stack = [[-1, 0, -1]]
            
            for i, h in enumerate(heights):
                while stack[-1][2] >= h:
                    stack.pop()
                idx, res, _ = stack[-1]
                res += (i-idx) * h
                cnt += res
                stack.append([i, res, h])
        
        return cnt
        
        
# @lc code=end

