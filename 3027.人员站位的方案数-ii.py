#
# @lc app=leetcode.cn id=3027 lang=python
#
# [3027] 人员站位的方案数 II
#

# @lc code=start
class Solution(object):
    def numberOfPairs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda x: (x[0], -x[1]))
        res = 0
        for i in range(len(points)):
            cur_max = -1000000001
            for j in range(i+1, len(points)):
                if points[j][1] > points[i][1]:
                    continue
                else:
                    if cur_max < points[j][1]:
                        cur_max = points[j][1]
                        res += 1
                    else:
                        continue
        return res
# @lc code=end

