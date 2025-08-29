class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n % 2 != 0:
            return 2 * (n // 2) + 1
        else:
            return 2 * (n // 2)