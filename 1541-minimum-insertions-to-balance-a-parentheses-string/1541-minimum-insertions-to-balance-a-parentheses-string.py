class Solution:
    def minInsertions(self, s: str) -> int:
        res, i, count = 0, 0, 0
        while i < len(s):
            if s[i] == "(":
                count += 1
            elif i + 1 < len(s) and s[i] + s[i + 1] == "))":
                if count:
                    count -= 1
                else:
                    res += 1
                i += 1
            else:
                if count > 0:
                    res += 1
                    count -= 1
                else:
                    res += 2
            i += 1
        return res + count * 2