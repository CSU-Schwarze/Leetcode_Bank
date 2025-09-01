#
# @lc app=leetcode.cn id=37 lang=python
#
# [37] 解数独
#

# @lc code=start
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def dfs(pos):
            if pos >= len(spaces):
                return True
            i, j = spaces[pos]
            for digit in range(9):
                if row[i][digit] or column[j][digit] or block[i // 3][j // 3][digit]:
                    continue
                else:
                    row[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = True
                    board[i][j] = str(digit+1)
                    if dfs(pos+1):
                        return True
                    row[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = False


        row = [[False] * 9 for _ in range(9)]
        column = [[False] * 9 for _ in range(9)]
        block = [[[False] * 9 for _ in range(3)] for _ in range(3)]
        spaces = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    spaces.append((i, j))
                else:
                    digit = int(board[i][j]) - 1
                    row[i][digit] = True
                    column[j][digit] = True
                    block[i // 3][j // 3][digit] = True
        #print("spaces:", len(spaces))
        dfs(0)
        
# @lc code=end

