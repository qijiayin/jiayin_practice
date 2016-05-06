#257 binary-tree-paths/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def path(self, root, s, res):
        if root == None:
            return res

        s += str(root.val)
        if root.left == root.right == None:
            res.append(s)
        if root.left != None :
            res = self.path(root.left, s+"->", res)

        if root.right != None :

            res = self.path(root.right, s+"->", res)
        return res




    def binaryTreePaths(self, root):
        res = []
        s = ""
        if root == None :
            return res
        return self.path(root, s, res)
