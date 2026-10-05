class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        def helper(l: int, r: int) -> int:
            res = bal = 0
            st = l
            for i in range(st, r):
                bal += 1 if s[i] == '(' else -1
                if bal == 0:
                    if i - st == 1:
                        res += 1
                    else:
                        res += 2 * helper(st + 1, i)
                    st = i + 1
            return res
        return helper(0, len(s))