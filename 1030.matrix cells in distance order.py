class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        
        res = []
        dist = []
        for r in range(R):
            for c in range(C):
                dist.append((abs(r - r0) + abs(c - c0)))
                res.append([r,c])
        dist, res = zip(*sorted(zip(dist,res)))    
        
        #operator zip(*the_list)unpack the sorted list
        
      
        return res
    
    