#
# @lc app=leetcode.cn id=4 lang=python
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1, len2 = len(nums1), len(nums2)
        if len1 > len2:
            return self.findMedianSortedArrays(nums2, nums1)
        inf = 2 ** 31

        left, right = 0, len1
        med1, med2 = 0, 0
        while left <= right:
            i = (left+right)//2
            j = (len1+len2+1)//2-i
            
            n_i = -inf if i == 0 else nums1[i-1]
            n_i1 = inf if i == len1 else nums1[i]
            n_j = -inf if j == 0 else nums2[j-1]
            n_j1 = inf if j == len2 else nums2[j]
            
            if n_i > n_j1:
                right = i-1
            else:
                left = i+1
                med1, med2 = max(n_i, n_j), min(n_i1, n_j1)
                
        if (len1+len2) % 2 == 0:
            return (med1+med2) / 2.0
        else:
            return med1
                
                    
                
        
# @lc code=end

