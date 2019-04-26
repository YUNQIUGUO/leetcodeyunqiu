class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #dynamic programming  O(n^2)
        #intialization
        L = []
        n = len(nums)
        if (n == 0)  :
            return 0
        else: 
            for i in range(n):
                L.append(1)
        #print(L)
                # bottom-up 
            for i in range(len(nums)-1,-1,-1):
                for j in range(i+1,n):
                    if ((nums[j] > nums[i]) and (L[j] + 1 > L[i])):
                        L[i] = L[j]+1
            return(max(L))
        
        #next time try O(nlogn)             
        
            
        