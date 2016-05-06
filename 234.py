#234 palindrome-linked-list/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def head_push(self,head, node):
        if head == None:
            node.next = None
            head = node
        else:
            node.next = head
            head = node
        return head

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None :
            return True

        ptr = head
        n = 0
        fst_half = snd_half = None
        while ptr!= None :
            n += 1
            ptr = ptr.next

        for i in range(n / 2):
            node = head
            head = head.next
            fst_half = self.head_push(fst_half, node)
        if n % 2 != 0 :
            snd_half = head.next
        else:
            snd_half = head



        while fst_half != None and snd_half != None :
            if fst_half.val != snd_half.val :
                return False
            fst_half = fst_half.next
            snd_half = snd_half.next
        return True
