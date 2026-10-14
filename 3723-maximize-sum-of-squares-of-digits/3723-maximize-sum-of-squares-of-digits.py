class Solution:
    def maxSumOfSquares(self, n: int, s: int) -> str:
        if s > 9*n: return ""
        a = []
        while s > 0:
            d = min(9, s)
            a.append(str(d))
            s -= d
        while len(a) < n: a.append('0')
        return "".join(a)