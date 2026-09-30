class Solution:
    def maxSubArray(self, nums):
        ms=nums[0]
        s=0
        for i in nums:
            s=s+i
            if s>ms:
                ms=s
            if s<0:
                s=0    
        return ms        
