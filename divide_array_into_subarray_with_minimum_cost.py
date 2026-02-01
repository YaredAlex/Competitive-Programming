from typing import List
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        
        ans = float("inf")
        #brute force solution to find all pissible combination of minimum sum
        for i in range(1,len(nums)):
            for j in range(i+1,len(nums)):
                cost = nums[0]+nums[i]+nums[j]
                ans = min(ans,cost)
        return ans