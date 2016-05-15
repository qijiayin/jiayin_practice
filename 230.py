#230 kth-smallest-element-in-a-bst/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def kth(self, root,  idx,  k, kthNode):

        if  root == None or kthNode != None:
            return  idx,kthNode

        if root.left != None:
            idx, kthNode = self.kth(root.left, idx, k,kthNode)
            if kthNode != None:
                return idx, kthNode
        idx += 1

        if  idx  == k  :
            kthNode = root
            return idx, kthNode

        if root.right != None:
            idx, kthNode = self.kth(root.right,  idx,  k, kthNode)





    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        kthNode = None
        idx , kthNode = self.kth(root, 0, k, kthNode)
        return kthNode.val
