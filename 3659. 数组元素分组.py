class Solution(object):
    def partitionArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) % k > 0:
            return False
        else:
            n = len(nums) // k
            cnt = {}
            for i in nums:
                if not cnt.has_key(i):
                    cnt[i] = 0
                cnt[i] += 1
                if cnt[i] > n:
                    return False
            return True