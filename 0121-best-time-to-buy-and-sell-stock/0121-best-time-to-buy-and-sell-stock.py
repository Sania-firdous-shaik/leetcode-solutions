class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi=9999999999
        ma=-9999999999
        for i in prices:
            mi=min(mi,i)
            ma=max(ma,i-mi)
        return ma    
