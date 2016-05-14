# 328 odd-even-linked-list/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def push(self, head, tail, t):
        if t == None :
            return head,tail
        t.next = None
        if head == None :
            head = tail = t
        else:
            tail.next = t
            tail = t
        return head,tail

    def merge(self, head1, tail1, head2, tail2):
        if head1 == None:
            return head2
        if head2 == None:
            return head1
        tail1.next = head2
        return head1


    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        oddHead = oddTail = evenHead = evenTail = None
        ptr = head
        i = 1
        while (ptr != None):
            nxt = ptr.next
            if i % 2 != 0 :
                oddHead, oddTail = self.push(oddHead, oddTail, ptr)
                print "odd:", ptr.val, i, oddHead.val, oddTail.val
            else:
                evenHead, evenTail = self.push(evenHead, evenTail, ptr)
                print "even:",ptr.val, i, evenHead.val, evenTail.val

            ptr = nxt
            i += 1

        return self.merge(oddHead, oddTail, evenHead, evenTail)
