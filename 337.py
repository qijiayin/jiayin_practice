#337 house-robber-iii/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#[2,1,3,null,4]
#[4,1,null,2,null,3]

class Solution(object):
    def robImp(self, root):
        if root == None:
            return 0, 0
        left_node, left_subtree = self.robImp(root.left)
        right_node, right_subtree = self.robImp(root.right)

        node =  root.val + left_subtree + right_subtree
        subtree = max(left_node, left_subtree) + max( right_node, right_subtree)

        return node, subtree

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root == None :
            return 0
        root_node, root_subtree = self.robImp(root)
        return max(root_node, root_subtree)
