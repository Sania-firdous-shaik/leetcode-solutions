class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1) 
        for i in range(n): 
            prefix[i + 1] = prefix[i] + nums[i] 
        
        minSum = float('inf')
        for length in range(l, r + 1):
            for start in range(n - length + 1):
                end = start + length
                currSum = prefix[end] - prefix[start]

                if currSum > 0:
                    minSum = min(minSum, currSum)

        return minSum if minSum != float('inf') else -1
                




