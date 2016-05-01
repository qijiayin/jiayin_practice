#111 minimum-depth-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):


    def minDepthHelper(self, root, curDep):
        curDep += 1
        if root.left == root.right == None :
            return curDep
        if root.left == None :
            return self.minDepthHelper(root.right, curDep)
        if root.right == None:
            return self.minDepthHelper(root.left, curDep)
        return min(self.minDepthHelper(root.left, curDep), self.minDepthHelper(root.right, curDep))


    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None : return 0
        return self.minDepthHelper(root, 0)
