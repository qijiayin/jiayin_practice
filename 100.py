class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if ((p==None) != (q==None)) :
            return False
        if (p==None and q==None):
            return True
        return p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        
