class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        p = len(nums) - 1
        while p > 0 and nums[p - 1] >= nums[p]:
            p -= 1
        if p == 0:
            nums.reverse()
            return
        q = len(nums) - 1
        while q >= p and nums[q] <= nums[p - 1]:
            q -= 1
        nums[p - 1], nums[q] = nums[q], nums[p - 1]
        nums[p:] = reversed(nums[p:])