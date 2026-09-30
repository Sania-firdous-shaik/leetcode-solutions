class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []
        for ch in num:
            while st and k > 0 and st[-1] > ch:
                st.pop()
                k -= 1
            st.append(ch)
        st = st[:-k] if k > 0 else st
        ans = ''.join(st).lstrip('0')
        return ans if ans else '0'
        