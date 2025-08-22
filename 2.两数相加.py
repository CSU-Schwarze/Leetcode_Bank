#
# @lc app=leetcode.cn id=2 lang=python
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = l1
        while l1 or l2:
            if not l1:
                l1 = ListNode(0)
            if not l2:
                l2 = ListNode(0)
            l1.val += l2.val
            if l1.val >= 10:
                l1.val -= 10
                if not l1.next:
                    l1.next = ListNode(0)
                l1.next.val += 1
            if not l1.next and l2.next:
                l1.next = ListNode(0)
            if not l1.next and not l2.next:
                return head
            l1, l2 = l1.next, l2.next
        
# @lc code=end

