#206 Reverse Linked List
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x,n=None):
         self.val = x
         self.next = n

class Solution(object):
    def popList(self,head):
        if head == None:
            return None;
        t = head
        head=t.next
        t.next=None
        return head,t

    def pushList(self,head,t):
        if head==None:
            head=t;
            return head
        t.next=head
        head=t
        return head

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = None
        while head != None:
            head,t = self.popList(head)
            res = self.pushList(res,t)
        return res

def pushbackList(head, t):
    if head == None:
        return t

    tail = head
    while tail.next != None :
        tail = tail.next
    tail.next = t;
    t.next = None

    return head

def makeListNode(l):
    head = None
    for x in l:
        t = ListNode(x)
        head = pushbackList(head,t)
    return head

def printList(head):
    while head != None:
        print "%d ," %head.val,
        head = head.next
'''
a=ListNode(1)
b=ListNode(2,a)
c=ListNode(3,b)
'''

s=Solution()
l=[1,2,3]
mylist=makeListNode(l)
printList(mylist)
printList(s.reverseList(mylist))
