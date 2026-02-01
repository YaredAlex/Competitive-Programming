from typing import List
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        
        ans = float("inf")
        #brute force solution to find all pissible combination of minimum sum
        for i in range(1,len(nums)):
            for j in range(i+1,len(nums)):
                cost = nums[0]+nums[i]+nums[j]
                ans = min(ans,cost)

        # optimized solution
        # get the first element since it is not going to be changed
        first = nums[0]
        # sort the array
        nums.sort()
        # return the sum of the first two number in sorted array and first number before sorting 
        # return first+nums[0]+nums[1]
        return ans