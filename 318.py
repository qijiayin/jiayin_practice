#318 maximum-product-of-word-lengths/

class Solution(object):
    def hasCommon(self,r1, r2):
        for i in range(256) :
            if r1[i] == 1 and  r1[i] == r2[i] :
                return True
        return False

    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        n = len(words)
        if n < 2 :
            return 0
        record = [ [ 0 for i in range(256) ] for j in range(n)]

        for i in range(n):
            word = words[i]
            for j in range(len(word)) :
                record[i][ord(word[j])] = 1

        maxVal = 0
        for i in range(n) :
            for j in range(i+1, n):
                if self.hasCommon(record[i], record[j]) == True :
                    continue
                else:
                    
                    maxVal = max(maxVal, len(words[i]) * len(words[j]) )
        return maxVal
