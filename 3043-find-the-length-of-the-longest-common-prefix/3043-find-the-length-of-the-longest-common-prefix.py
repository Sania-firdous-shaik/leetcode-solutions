class Solution:
    def longestCommonPrefix(self, arr1, arr2):
        prefixes = set()
        for num in arr1:
            while num > 0:
                prefixes.add(num)
                num //= 10
        ans = 0
        for num in arr2:
            while num > 0:
                if num in prefixes:
                    ans = max(ans, len(str(num)))
                    break
                num //= 10
        return ans