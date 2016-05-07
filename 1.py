#1 two-sum/
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mapping = {}
        for i in range(len(nums)):
            idx = mapping.get(nums[i])
            if idx == None:
                mapping[nums[i]] = [i]

            else :
                mapping[nums[i]].append(i)

        for i in range(len(nums)):
            idx_i_list = mapping[nums[i]]
            if nums[i] == target - nums[i]:
                if len(idx_i_list) >= 2 :
                    return [idx_i_list[0], idx_i_list[1]]
            else:
                idx_j_list = mapping.get(target - nums[i])
                if idx_j_list != None :
                    return [idx_i_list[0], idx_j_list[0]]
        return []
