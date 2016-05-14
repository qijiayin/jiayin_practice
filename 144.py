#144 binary-tree-preorder-traversal/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None :
            return []
        res = []
        stack = [root]
        while len(stack) > 0 :
            p = stack.pop()
            res.append(p.val)
            if p.right != None:
                stack.append(p.right)
            if p.left != None:
                stack.append(p.left)
        return res
