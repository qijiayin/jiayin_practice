#232 implement-queue-using-stacks/
class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack1.append(x)


    def pop(self):
        """
        :rtype: nothing
        """
        self.stack2=self.stack1[::-1]
        self.stack2.pop()
        self.stack1=self.stack2[::-1]


    def peek(self):
        """
        :rtype: int
        """
        self.stack2=self.stack1[::-1]
        r = self.stack2[-1]
        self.stack1=self.stack2[::-1]
        return r


    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack1) == 0
