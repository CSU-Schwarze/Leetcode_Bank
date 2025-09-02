#
# @lc app=leetcode.cn id=17 lang=python
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def dfs(idx, str):
            if idx == len(digits):
                ans.append(str)
                return
            for c in phone[digits[idx]]:
                dfs(idx+1, str+c)
        ans = []
        if not digits:
            return ans
        phone = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno',
                 '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        dfs(0, "")
        return ans
        
# @lc code=end

