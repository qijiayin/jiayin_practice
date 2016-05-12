#347 top-k-frequent-elements/
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq_mapping = {}

        for i in range(len(nums)) :
            v = freq_mapping.get(nums[i])
            if v == None:
                freq_mapping[nums[i]] =  1
            else :
                freq_mapping[nums[i]] +=  1

        mapping = [[val, key] for  key, val in freq_mapping.iteritems() ]
