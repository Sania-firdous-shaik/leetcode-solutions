class Solution:
    def isPalindrome(self, s: str) -> bool:
        r=''
        d=''
        s=s.lower()
        for i in s:
            if i.isalnum():
                d=d+i
                r=i+r
        if d==r:
            return True
        else:
            return False   
        