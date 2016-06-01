#129 sum-root-to-leaf-numbers/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumImp(self, cur_sum, root, res):
        if root == None :
            return res

        cur_sum *= 10
        cur_sum += int(root.val)
        print root.val, cur_sum, res
        if root.left == None and root.right == None:
            res += cur_sum
            return  res

        if root.left != None:
            res =  self.sumImp(cur_sum, root.left, res)
        if root.right != None:
            res =  self.sumImp(cur_sum, root.right, res)
        return res


    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        res = 0
        res = self.sumImp(0, root, res)
        return res
