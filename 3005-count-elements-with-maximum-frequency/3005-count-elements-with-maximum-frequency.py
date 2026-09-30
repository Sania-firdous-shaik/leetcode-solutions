from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums):
        freq = Counter(nums)

        mx = max(freq.values())

        total = 0
        for v in freq.values():
            if v == mx:
                total += v

        return total