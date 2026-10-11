class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = 0
        for i, x in enumerate(nums, start=1):
            if n % i == 0:
                total_sum += x * x
        return total_sum