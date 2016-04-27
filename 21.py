# 21 merge-two-sorted-lists/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def push(self,head, tail, t ):
        if t == None:
            return head, tail
        if head == None:
                head = tail = t
        else:
                tail.next = t
                tail = t
        return head, tail

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = tail = None

        while ( l1 != None and l2 != None ) :
            if l1.val < l2.val :
                t = l1
                l1 = l1.next

            else:
                t = l2
                l2 = l2.next
            t.next = None
            head, tail = self.push(head, tail, t )

        if l1 != None : head, tail =self.push(head, tail, l1)
        if l2 != None : head, tail =self.push(head, tail, l2)
        return head
