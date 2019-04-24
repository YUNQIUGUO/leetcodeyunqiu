class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #sort the input array num
        nums_sorted = sorted(nums)
        print(nums_sorted)
        
        l = 0
        r = len(nums_sorted) - 1
        res = []
        
        #O(n) time complexity lagorithm with 2sum problem given a sorted array
        while(l != r):
            if (nums_sorted[l] + nums_sorted[r] == target):
                a = nums_sorted[l]
                b = nums_sorted[r]
                if (a != b):
                    i = nums.index(a)
                    j = nums.index(b)
                    res.append(i)
                    res.append(j)
                else:
                    for k in range(0,len(nums)):
                        if (nums[k] == a):
                            res.append(k)
                return res
            elif (nums_sorted[l] + nums_sorted[r]  > target):
                r = r - 1
            else:
                l = l + 1
                
        return res