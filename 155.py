#155 min-stack/
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None



    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        y = ListNode(x)
        if self.min == None:
            self.min = y
        elif y.val < self.min.val :
            y.next = self.min
            self.min = y

        self.stack.append(y)

    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack) != 0:
            y = self.stack.pop()
            if self.min == y:
                self.min = y.next



    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return 0
        return self.stack[-1].val

    def getMin(self):
        """
        :rtype: int
        """
        return self.min.val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
