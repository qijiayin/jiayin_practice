#108 convert-sorted-array-to-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def BST(self, nums, i, j):
        if i > j :
            return None
        mid = (i+j) / 2
        root = TreeNode(nums[mid])
        root.left = self.BST(nums, i, mid -1 )
        root.right = self.BST(nums, mid + 1, j)
        return root

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.BST(nums, 0, len(nums)-1)
