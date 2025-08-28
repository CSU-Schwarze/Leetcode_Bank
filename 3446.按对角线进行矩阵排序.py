#
# @lc app=leetcode.cn id=3446 lang=python
#
# [3446] 按对角线进行矩阵排序
#

# @lc code=start
class Solution(object):
    def sortMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        l = len(grid[0])
        #lower diagonal
        for i in range(len(grid)):
            temp = []
            x, y = i, 0
            while x < len(grid) and y < l:
                temp.append(grid[x][y])
                x += 1
                y += 1
            temp.sort(reverse=True)
            x, y = i, 0
            for val in temp:
                grid[x][y] = val
                x += 1
                y += 1
        #upper diagonal
        for i in range(1, l):
            temp = []
            x, y = 0, i
            while x < len(grid) and y < l:
                temp.append(grid[x][y])
                x += 1
                y += 1
            temp.sort()
            x, y = 0, i
            for val in temp:
                grid[x][y] = val
                x += 1
                y += 1
        return grid
           
        
# @lc code=end

