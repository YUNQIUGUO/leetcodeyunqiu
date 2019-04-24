class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # a_i + a_j + a_k = 0
        res = []
        if  (len(nums) < 3) :
            return res
        else:
            nums_sorted = nums[:]
            nums_sorted.sort()
            #print(nums_sorted)
            #convert to 2-sum problem
            for i in range (0, len(nums_sorted)):
                target = - nums_sorted[i]
                #print(-target)
                if (i != 0) and (nums_sorted[i] == nums_sorted[i-1]):
                    continue    
                nums_sorted_new = nums_sorted[i:]
                #print(nums_sorted_new)
                # find a_i + a_j = - a_k using two pointers
                l = 1
                r = len(nums_sorted_new) - 1
                while (l < r):
                    sol = []
                    if (nums_sorted_new[l] + nums_sorted_new[r] == target):
                        a1 = nums_sorted_new[l]
                        a2 = nums_sorted_new[r]
                        a3 = -target
                        sol = [a3,a1,a2]
                        #print(l,r)
                        #print(sol)
                        res.append(sol)
                        l = l + 1
                        r = r - 1
                        while (l <= r) and (nums_sorted_new[l] == nums_sorted_new[l-1]):   
                            l = l + 1
                            
                    elif (nums_sorted_new[l] + nums_sorted_new[r] > target):
                        r = r - 1
                    else:
                        l = l + 1
        return res
    