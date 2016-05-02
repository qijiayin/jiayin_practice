#19 remove-nth-node-from-end-of-list/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        ptr1 = ptr2 =  head
        while ptr1 != None and n > 0:
            ptr1 = ptr1.next
            n -= 1
        if n > 0 :
            return head
        if ptr1 == None :
            head = head.next
            return head
        while ptr1.next != None :
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        ptr2.next = ptr2.next.next
        return head
