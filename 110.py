#110 balanced-binary-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBal(self, root):
        if (root == None ) :
            return 0,True
        lheight, lres = self.isBal(root.left)
        rheight, rres = self.isBal(root.right)
        height = max(lheight, rheight) + 1
        res = False
        if lres and rres and abs(lheight - rheight) <= 1 :
            res = True
        return height, res

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        h, res =  self.isBal(root)
        return res
