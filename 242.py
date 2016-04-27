#242 valid-anagram/
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (len(s) != len(t)) : return False
        fst_count=[0 for i in range(0,256)]
        snd_count=[0 for i in range(0,256)]
        for i in range(0, len(s)):
            fst_count[ord(s[i])]+=1
            snd_count[ord(t[i])]+=1

        return fst_count == snd_count

s=Solution()
a="a"
b="b"
print s.isAnagram(a,b)
