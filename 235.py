# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 235 lowest-common-ancestor-of-a-binary-search-tree/
class Solution(object):
    def find(self, root, p, q):
        """
        rtype: has_p, has_q, lca
        """
        if root == None :
            return False, False, None

        lhas_p, lhas_q, llca = self.find( root.left, p, q )
        rhas_p, rhas_q, rlca = self.find( root.right, p, q )

        if llca  :
            return True, True, llca
        if rlca :
            return True, True, rlca

        has_p = lhas_p or  rhas_p or root == p
        has_q = lhas_q or  rhas_q or root == q

        if  has_p and has_q :
            lca = root
        else:
            lca = None

        return has_p, has_q, lca




    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if (root==None or p==None or q==None):
            return None
        if (p == q):
            return p
        has_p, has_q, lca =  self.find(root, p , q )
        return lca
