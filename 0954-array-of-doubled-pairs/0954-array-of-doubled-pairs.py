from collections import Counter
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        dp = Counter()
        arr.sort()
        for i in range(len(arr)):
            dp[arr[i]] += 1 
        count = 0
        print("arr--->",arr)
        for i in range(len(arr)):
            flag = False
            dp[arr[i]] -= 1
            if dp[arr[i]] >= 0 and dp[2*arr[i]] > 0:
                flag = True
                dp[2*arr[i]] -= 1
                count += 1
            if not flag:
                dp[arr[i]] += 1
        print("count--->",count)
        return count == len(arr)/2
