class Solution:
    def isValid(self,s:str)->bool:
        if len(s)%2:return False
        st,m=[],{')':'(','}':'{',']':'['}
        for c in s:
            if c in m:
                if not st or st.pop()!=m[c]:
                    return False
            else:
                st.append(c)
        return not st