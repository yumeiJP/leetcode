#
# @lc app=leetcode id=141 lang=python
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        slow = head
        fast = head

        if head is None:
            return False

        if head.next is None:
            return False

        slow = slow.next
        fast = fast.next.next

        while slow!=fast and fast:

            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        
        if slow == fast:
            return True
        else:
            return False
        
# @lc code=end

