class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n=len(nums)
        count=0
        nums.sort()
        x=nums[n//2]
        for i in nums:
            count+=abs(i-x)
        return count 
        

        
        