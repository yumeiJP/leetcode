#
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def convertToNumber(self, ls):
        length = len(ls)
        count = 0
        for i in range(length):
            count += ls[i]*(10**(i))
        return count
    
    def constructLinkedList(self, ls):
        dummy = ListNode(0)
        current = dummy

        for num in ls:
            current.next = ListNode(num)
            current = current.next
        
        return dummy.next



    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        b1 = []
        b2 = []

        while l1:
            b1.append(l1.val)
            l1 = l1.next

        while l2:
            b2.append(l2.val)
            l2 = l2.next


        n1 = self.convertToNumber(b1)
        n2 = self.convertToNumber(b2)

        sum = n1+n2

        sum = str(sum)

        sum = list(map(int, sum))
        sum.reverse()
        return self.constructLinkedList(sum)
        

# @lc code=end

