class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        #dynamic programming for rotation is not allowed solution
        n = len(envelopes)
        L = []
        if (n == 0) :
            return 0
        
        res = 1
        for i in range(n):  #initialization
            L.append(1)
            
        envelopes.sort()       #sort by the width
            #print(envelopes)
        for i in range(n):
            for j in range(i):
                if ((envelopes[i][0] > envelopes[j][0]) and (envelopes[i][1]> envelopes[j][1])):
                    L[i] = max(L[j]+1,L[i])
                    res = max(res,L[i])
                            
                            
        return res