#
# @lc app=leetcode.cn id=3 lang=python
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        len = 0
        left, right = 0, 0
        hash = {}
        for i, c in enumerate(s):
            if c in hash and hash[c] >= left:
                left = hash[c] + 1
            hash[c] = i
            right = i
            len = max(len, right-left+1)
        return len
            
        
# @lc code=end

