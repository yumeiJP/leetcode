#
# @lc app=leetcode id=206 lang=python
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        current = head

        if not current:
            return head

        pastnode = ListNode(current.val)
        current = current.next

        while current:
            newnode = ListNode(current.val, pastnode)
            pastnode = newnode
            current = current.next
        
        return pastnode
            
             
        
# @lc code=end

