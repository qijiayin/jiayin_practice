#!/usr/bin/env python
#283. Move Zeroes move-zeroes
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        quick sort
        [0-i] !=0
        [i+1,j] ==0
        start:i=-1 j=i+1
        """
        i=-1
        while (i+1<len(nums) and nums[i+1]) :
            i+=1
        j=i+1
        while j<len(nums):
            if nums[j] == 0 :
                j+=1
            else:
                tmp=nums[i+1]
                nums[i+1]=nums[j]
                nums[j]=0
                i+=1
                j+=1


def main():
    s=Solution()
    nums=[0,1]
    s.moveZeroes(nums)
    print nums

if __name__ == "__main__":
    main()
