class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        cache = {0: -1}
        rem = 0
        for i in range(len(nums)):
            rem += nums[i]
            rem %= k
            if rem not in cache:
                cache[rem] = i
            elif i - cache[rem] >= 2:
                return True
        return False