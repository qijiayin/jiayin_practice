#241 different-ways-to-add-parentheses/
class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if len(input) == 0 :
            return []
        if len(input) == 1:
            return int(input[0])

        opers = []
        nums = []

        for c in input :
            if c == '+' or c == '-' or c == '*':
                opers.append(c)
            else:
                nums.append(int(c))
        res = [[0 for i in nums]  for j in nums ]

        result = []
        for i in range(len(nums)) :
            res[i][i] = nums[i]

        for k in range(0, len(nums)):
            for i in range(len(nums)):
                j = i + k
                if j >= len(nums):
                    continue
                for r in range(i, j):
                    oper = opers[r]
                    if oper == "+":
                        res[i][j] = res[i][r] + res[r+1][j]
                    elif oper == "-":
                        res[i][j] = res[i][r] - res[r+1][j]
                    elif oper == "*":
                        res[i][j] = res[i][r] * res[r+1][j]
                    if i==0 and j == len(nums)-1 :
                        result.append(res[i][j])

        return result
