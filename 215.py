#215 kth-largest-element-in-an-array/

class Solution(object):

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        n = 0

        for x in nums :
            if n < k :
                heapq.heappush(heap, x )
                n += 1

            else:
                t = heap[0]
                if x > t :
                    heapq.heappop(heap)
                    heapq.heappush(heap, x )

        return heap[0]

        
class Node(object):
    def __init__(self, x):
        self.val = x
    def __lt__(self, other):
        return self.val > other.val

class Solution(object):

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        idx = 0
        heap = [ Node(x) for x in nums]
        heapq.heapify(heap)
        res = Node(nums[0])
        while idx < k :
            res = heapq.heappop(heap)
            idx += 1
        return res.val
