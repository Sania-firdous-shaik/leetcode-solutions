class Solution:
    def minElement(self, nums: List[int]) -> int:
        min=999
        for i in nums:
            s=0
            while i!=0:
                r=i%10
                s=s+r
                i=i//10
            if s<min:
                min=s
        return min           
