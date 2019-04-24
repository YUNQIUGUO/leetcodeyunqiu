
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #divide and conquer
        res = 0
        n = len(nums)
        print(n)
        if (n == 0):
            return 0
        if (n == 1):
            return nums[0]
        else:
            
            if (n % 2 == 0):
                left_arr = nums[: n/2]
                #print(left_arr)
                right_arr = nums[n/2:]
                #print(right_arr)
                mid = n/2 - 1
            else:
                left_arr = nums[: (n-1)/2 + 1]
                #print(left_arr)
                right_arr = nums[(n-1)/2 + 1:]
                #print(right_arr)
                mid = n/2
            
            s1 = self.maxSubArray(left_arr)
            s2 = self.maxSubArray(right_arr) 
            s3 = self.crossSubArray(nums,0,mid,n)
         
            print(s1,s2,s3)
           
            res = max(s1,s2,s3)
        
        return res
    
    def crossSubArray(self,a,low,mid,high):
        #modify for small length cases?
        left_sum = float("-inf")
        s = 0
        for i in range (mid, low-1, -1):
            s += a[i]
            if s > left_sum:
                left_sum = s
                
        right_sum = float("-inf")
        s = 0 
        for i in range(mid+1,high):
            s+= a[i]
            if s > right_sum:
                right_sum = s
                
        return left_sum + right_sum