#94 binary-tree-inorder-traversal/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        res = []
        stack = []
        p = root

        
        while len(stack) > 0   or  p != None :
            while p != None:
                stack.append(p)
                p = p.left
            p = stack.pop()
            res.append(p.val)
            p = p.right

        return res
