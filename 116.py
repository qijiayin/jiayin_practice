#116 populating-next-right-pointers-in-each-node/
# Definition for binary tree with next pointer.
import collections
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """

        if root == None:
            return
        cur_que = next_que = collections.deque()
        cur_que.append(root)
        #for y in cur_que: print y.val
        while len(cur_que) > 0 :
            next_que.clear()
            pre_node = None
            for y in cur_que: print y.val
            while len(cur_que) > 0:
                node = cur_que[0]
                if node.left != None:
                    next_que.append(node.left)
                if node.right != None:
                    next_que.append(node.right)

                x = cur_que.popleft()
                if pre_node != None:
                    pre_node.next = x
                pre_node = x
            for y in next_que: print y.val
            cur_que = next_que

root = TreeNode(1)
root.left = TreeNode(2)
root.right= TreeNode(3)
s= Solution()
s.connect(root)
