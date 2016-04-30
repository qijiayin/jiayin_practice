#102 binary-tree-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if root == None : return res
        cur_level = [root]
        while len(cur_level) > 0 :
            next_level = []
            for node in cur_level :
                if node.left != None :
                    next_level.append(node.left)
                if node.right != None :
                    next_level.append(node.right)
            res.append([p.val for p in cur_level])
            cur_level = next_level
        return res
