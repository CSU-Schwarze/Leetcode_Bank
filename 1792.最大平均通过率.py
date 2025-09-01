#
# @lc app=leetcode.cn id=1792 lang=python
#
# [1792] 最大平均通过率
#

# @lc code=start
class Solution(object):
    class Entry():
        def __init__(self, p, t):
            self.p = p
            self.t = t
        def __lt__(self, b):
            return (self.t+1) * self.t * (b.t - b.p) < (b.t+1) * b.t * (self.t- self.p)
            
        
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        h = [self.Entry(p, t) for p, t in classes]
        import heapq as heap
        heap.heapify(h)
        for _ in range(extraStudents):
            heap.heapreplace(h, self.Entry(h[0].p+1, h[0].t+1))
        return sum(e.p * 1.0 / e.t for e in h) / len(h)
# @lc code=end

