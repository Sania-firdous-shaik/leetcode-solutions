class Solution:
    def processStr(self, s: str) -> str:
        r=''
        for i in s:
            if i.isalpha():
                r=r+i
            elif i=="#":
                r=r+r
            elif i=="%":
                r=r[::-1]
            elif i=="*":
                r=r[:-1]
        return r                    