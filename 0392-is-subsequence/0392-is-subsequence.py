class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        subseq_len =len(s)
        if subseq_len == 0:
            return True
        main_len = len(t)
        s_count = 0
        for i in range(main_len):
            if t[i] == s[s_count]:
                s_count += 1
        
            if s_count > subseq_len-1:
                return True
                
        return False