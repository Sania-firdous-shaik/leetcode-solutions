class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        a = []
        self.f(s, a, 0, 0, ['(', ')'])
        return a

    def f(self, s, a, i, j, p):
        c = 0
        for k in range(i, len(s)):
            if s[k] == p[0]: c += 1
            if s[k] == p[1]: c -= 1
            if c < 0:
                for x in range(j, k + 1):
                    if s[x] == p[1] and (x == j or s[x - 1] != p[1]):
                        self.f(s[:x] + s[x + 1:], a, k, x, p)
                return
        r = s[::-1]
        if p[0] == '(':
            self.f(r, a, 0, 0, [')', '('])
        else: a.append(r)