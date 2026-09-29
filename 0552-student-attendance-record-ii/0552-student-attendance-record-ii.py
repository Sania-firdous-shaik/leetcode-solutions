class Solution:
    def checkRecord(self, n: int) -> int:
        ai, ai1, ai2 = 3, 1, 0
        bi, bi1, bi2 = 2, 1, 1
        for i in range(1, n):
            ai, ai1, ai2 = (ai+bi+bi1+ai1+bi2+ai2) % int(1e9+7), ai, ai1
            bi, bi1, bi2 = (bi+bi1+bi2) % int(1e9+7), bi, bi1
        
        return ai