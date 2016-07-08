#331 verify-preorder-serialization-of-a-binary-tree/
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        pre = preorder.split(',')
        if len(pre) == 0 or pre[0] == '#':
            return True
        stack = [0]

        for idx in range(1, len(pre)) :
            while len(stack) > 0 and stack[-1] == 2:
                stack.pop()
                if len(stack) >0 :
                    stack[-1] += 1


            if pre[idx] == '#':
                if len(stack) > 0:
                    stack[-1] += 1
                else:
                    return False
            else:
                stack.append(0)



        while len(stack) > 0 and stack[-1] == 2:
                stack.pop()
                if len(stack) > 0 :
                    stack[-1] += 1

        return len(stack) == 0
