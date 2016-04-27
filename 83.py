# 83 remove-duplicates-from-sorted-list/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
 
        
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        cur = head
        while ( cur != None ):
            if pre != None and pre.val == cur.val :
                pre.next = cur.next
                cur = None
                cur = pre.next
            else :
                pre = cur
                cur = cur.next
        return head 
         