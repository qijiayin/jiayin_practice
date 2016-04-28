# 101 symmetric-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None or root.left == root.right == None : return true
        if root.left == None != root.right == None : return False
        p = root.left
        q = root.right
        plist=[]
        qlist=[]

        while p != None and q != None :

            while p != None :
                plist.append(p)
                p = p.left
            ptop = plist.pop()
            p = ptop.right

            while q != None :
                qlist.append(q)
                q = q.left
            qtop = qlist.pop()
            q = qtop.right

            if ptop.val != qtop.val:
                return False

        return plist == qlist
