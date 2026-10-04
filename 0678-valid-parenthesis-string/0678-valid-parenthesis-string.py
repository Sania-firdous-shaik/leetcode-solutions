class Solution:
    def checkValidString(self, s: str) -> bool:
        mn=mx=0
        for x in s:
            mn+=((x=='(')<<1)-1; mx+=((x!=')')<<1)-1
            if mx<0: return False
            mn=max(mn,0)
        return mn==0