#345 reverse-vowels-of-a-string/
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = ['a','e', 'i' , 'o', 'u']
        vowel_dict = {x:True for x in l}
        i = 0
        j = len(s) - 1
        slist = [ s[x] for x in range(0, len(s)) ]
        while i < j :
            if slist[i].lower() not in vowel_dict.keys() :
                i += 1
                continue
            if slist[j].lower() not in vowel_dict.keys() :
                j -= 1
                continue
            tmp = slist[i]
            slist[i] = slist[j]
            slist[j] = tmp
            i += 1
            j -= 1

        return ''.join(slist)
