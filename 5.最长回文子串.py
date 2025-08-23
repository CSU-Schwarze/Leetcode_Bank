#
# @lc app=leetcode.cn id=5 lang=python
#
# [5] 最长回文子串
#

# @lc code=start
import numpy as np
class Solution(object):
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        if l < 2:
            return s
        m = [[False] * l for _ in range(l)]
        #m = np.full((l, l), False)
        for i in range(l):
            m[i][i] = True
        max_len, pivot = 1, 0
        for i in range(l-1, -1, -1):
            for j in range(i+1, l):
                if s[i] == s[j]:
                    if j-i == 1:
                        m[i][j] = True
                    else:
                        m[i][j] = m[i+1][j-1]
                else:
                    m[i][j] = False
                if m[i][j] and j-i+1 > max_len:
                    max_len = j-i+1
                    pivot = i
        return s[pivot:pivot+max_len]
# @lc code=end

