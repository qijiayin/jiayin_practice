#24 swap-nodes-in-pairs/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def push(self, head, tail, t):
        if t == None :
            return head, tail
        t.next = None
        if head == None:
            head = tail = t
        else :
            tail.next = t
            tail = t
        return head, tail

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        rhead = rtail = None

        while head!=None and head.next != None :
            tmp = head.next.next
            rhead, rtail = self.push(rhead, rtail, head.next)
            rhead, rtail = self.push(rhead, rtail, head)
            head = tmp
        rhead, rtail = self.push(rhead, rtail, head)
        return rhead
