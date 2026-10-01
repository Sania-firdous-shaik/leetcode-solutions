class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        cand1, cand2, count1, count2 = None, None, 0, 0
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = num, 1
            elif count2 == 0:
                cand2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        threshold = len(nums) // 3
        return [c for c in (cand1, cand2) if c is not None and nums.count(c) > threshold]