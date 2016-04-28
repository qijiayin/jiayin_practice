#101 symmetric-tree/
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
        [5,4,1,null,1,null,4,2,null,2,null]
        [1,2,2,null,3,null,3]
        """
        if root == None  : return True

        lstack = rstack = []
        if root.left != None : lstack=[root.left]
        if root.right != None : rstack=[root.right]

        while len(lstack) > 0  and len(rstack) > 0 :

            p = lstack.pop()
            q = rstack.pop()

            if p.val != q.val : return False
            if ( (p.left == None) != (q.right == None )  or ( p.right == None) != (q.left == None) ): return False

            if (p.right != None) : lstack.append( p.right)
            if (p.left != None) :  lstack.append( p.left )

            if (q.left !=None ) :  rstack.append( q.left )
            if (q.right != None) : rstack.append( q.right )


        return lstack == rstack
