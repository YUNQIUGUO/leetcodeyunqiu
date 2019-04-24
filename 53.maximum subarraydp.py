class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #dynamic programming
        # recursive solution:
        #MS[i] = max(MS[i-1]+ A[i], A[i])
        n = len(nums)
        if (n == 0):
            return 0
        elif (n == 1):
            return nums[0]
        else:
            MS = []
            MS.append(nums[0])
            for i in range(1,n):
                if (MS[i-1]+ nums[i] > nums[i]):
                    MS.append(MS[i-1]+ nums[i])
                else:
                    MS.append(nums[i])

        return max(MS)