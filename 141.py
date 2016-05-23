#141 linked-list-cycle/
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
        if head == None or head.next == None:
            return False
        fast = slow = head
        while fast != None and fast.next != None :
            fast = fast.next.next
            slow = slow.next

            if fast ==  slow:
                return True
        return False
