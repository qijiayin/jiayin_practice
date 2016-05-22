#199 binary-tree-right-side-view/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        fst_que = [root]
        res = []
        while len(fst_que) > 0 :
            res.append(fst_que[-1].val)
            snd_que = []

            for x in fst_que:
                if x.left != None:
                    snd_que.append(x.left)
                if x.right != None:
                    snd_que.append(x.right)
            fst_que = snd_que

        return res
