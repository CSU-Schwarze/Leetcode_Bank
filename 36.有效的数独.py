#
# @lc app=leetcode.cn id=36 lang=python
#
# [36] 有效的数独
#

# @lc code=start
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        hash_x, hash_y = [[False for _ in range(9)] for _ in range(9)], [[False for _ in range(9)] for _ in range(9)]
        hash_box = [[[False for _ in range(9)] for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j]) - 1
                    i_index, j_index = i // 3, j // 3
                    if hash_x[i][num] or hash_y[j][num] or hash_box[i_index][j_index][num]:
                        return False
                    else:
                        hash_x[i][num] = True
                        hash_y[j][num] = True
                        hash_box[i_index][j_index][num] = True
        return True
        
# @lc code=end

