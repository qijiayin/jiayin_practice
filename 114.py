#114 flatten-binary-tree-to-linked-list/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatImp(self, root):
        if root == None:
            return None
        left = right = None
        if root.left != None:
            left = self.flatten(root.left)
        if root.right != None:
            right = self.flatten(root.right)

        if left != None:
            print left.val
            left.right = right
            root.right = left
            root.left = None
        return root

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        root = self.flatImp(root)
