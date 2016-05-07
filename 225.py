#225 implement-stack-using-queues/
class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        import collections
        self.que1 = collections.deque()
        self.que2 = collections.deque()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.que1.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        while len(self.que1) > 1 :
            x = self.que1.popleft()
            self.que2.append(x)
        if len(self.que1) ==  1 :
            self.que1.pop()
        while (len(self.que2) > 0 ) :
            x = self.que2.popleft()
            self.que1.append(x)




    def top(self):
        """
        :rtype: int
        """
        while len(self.que1) > 1 :
            x = self.que1.popleft()
            self.que2.append(x)
        if len(self.que1) ==  1 :
            t = self.que1.pop()
            self.que2.append(t)
        while (len(self.que2) > 0 ) :
            x = self.que2.popleft()
            self.que1.append(x)
        return t

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.que1) == 0
