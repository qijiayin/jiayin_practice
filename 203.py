#203 remove-linked-list-elements/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None :
            return head
        cur = head
        pre = None
        while cur != None :
            if cur.val != val :
                pre = cur
                cur = cur.next
            else :
                toDel = cur
                if pre == None :
                    head = head.next

                else :
                    pre.next = cur.next
                cur = cur.next
                toDel.next = None
        return head
