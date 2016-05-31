#313 super-ugly-number/
import heapq

class Node(object):
    def __init__(self, value, index, prime):
        self.value = value
        self.index = index
        self.prime = prime

    def __lt__(self, other):
        return self.value < other.value

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        if n == 1:
            return 1

        res = [1]
        heap = []
        [heapq.heappush(heap, Node(x, 0, x)) for x in primes]

        while len(res) < n:
            next = heap[0]
            res.append(next.value)
            while len(heap) > 0 and next.value == res[-1]:
                heapq.heappop(heap)
                index = next.index + 1
                cur = Node(res[index] * next.prime, index, next.prime)
                print  next.value, next.prime, index, res[index],cur.value
                print res

                heapq.heappush(heap, cur)
                next = heap[0]

        return res[-1]
s=Solution()
primes=[2,3,5]
print s.nthSuperUglyNumber(10,primes)
