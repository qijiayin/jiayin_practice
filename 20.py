#20 valid-parentheses/
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        case:[])
        """
        if len(s) == 0 : return True
        stack=[]
        strmap = { ')':'(',  ']':'[',   '}':'{'}
        for i in range(0, len(s)):
            ch = s[i]

            if len(stack) > 0 and ch in strmap.keys() and stack[-1] == strmap[ch]:
                stack.pop()
            else:
                stack.append(ch)

        return len(stack) == 0
