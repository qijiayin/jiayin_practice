#107 binary-tree-level-order-traversal-ii/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import deque
        result = [[]]
        if root == None : return result
        que = [deque(), deque()]
        if root != None : que[0].append(root)
        idx = 0
        while len(que[idx]) > 0 :
            res = []
            while len(que[idx]) >0 :
                t = que[idx].popleft()
                if t.left != None :
                    que[1 - idx].append(t.left)
                if t.right != None:
                    que[1 - idx].append(t.right)
                res.append(t.val)
            result.append(res)
            idx = 1 - idx


        return result.reverse()
