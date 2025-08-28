#
# @lc app=leetcode.cn id=10 lang=python
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ls, lp = len(s), len(p)
        match = [[False for _ in range(lp+1)] for _ in range(ls+1)]
        match[0][0] = True
        for j in range(2, lp+1):
            if p[j-1] == '*':
                match[0][j] = match[0][j-2]
        for i in range(1, ls+1):
            for j in range(1, lp+1):
                # two cases: star or not
                # if star, then two cases: match 0 or match 1+
                if p[j-1] == '*':
                    match[i][j] = match[i][j-2] or (match[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.'))
                # not star
                else:
                    match[i][j] = match[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '.')
        
        return match[ls][lp]
            
# @lc code=end

