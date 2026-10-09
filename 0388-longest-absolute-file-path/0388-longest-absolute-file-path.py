class Solution:
    def lengthLongestPath(self, input: str) -> int:
        s, m = [0], 0
        for p in input.split("\n"):
            d = p.rfind("\t") + 1
            while d + 1 < len(s):
                s.pop()
            l = s[-1] + len(p) - d + 1
            s.append(l)
            if '.' in p:
                m = max(m, l - 1)
        return m