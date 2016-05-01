#160 intersection-of-two-linked-lists/
# Definition for singly-linked list.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None :
            return None
        if headA == headB : return headA
        ptra = headA
        ptrb = headB
        stepa = stepb = 0
        while ptra.next != None :
            ptra = ptra.next
            stepa += 1
        while ptrb.next != None :
            ptrb = ptrb.next
            stepb += 1
        if ptra != ptrb :
            return None

        if stepa > stepb :
            tmp = headA
            headA = headB
            headB = tmp
        for i in range(0, abs(stepb - stepa)):
            headB = headB.next
        while (headA != headB ):
            headA = headA.next
            headB = headB.next
        return headA

            
