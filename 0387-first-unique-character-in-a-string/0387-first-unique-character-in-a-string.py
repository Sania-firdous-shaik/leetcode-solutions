class Solution:
    def firstUniqChar(self, s: str) -> int:
        f = [0] * 26
        for c in s:
            f[ord(c) - 97] += 1
        for i, c in enumerate(s):
            if f[ord(c) - 97] == 1:
                return i
        return -1