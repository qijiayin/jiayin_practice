#226 invert-binary-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root==None: return None
        l=self.invertTree(root.left)
        r=self.invertTree(root.right)
        root.left=r
        root.right=l
        return root
