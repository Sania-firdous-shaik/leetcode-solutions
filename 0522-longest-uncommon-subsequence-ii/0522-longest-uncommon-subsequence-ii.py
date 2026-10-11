from collections import Counter
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def subseq(a, b):
            if len(a) >= len(b):
                return False
            i, j = 0, 0
            while i < len(a) and j < len(b):
                if a[i] == b[j]:
                    i += 1
                j += 1
            return i == len(a)
        count = Counter(strs)
        exclude = [s for s, c in count.items() if c > 1]
        check = [s for s, c in count.items() if c == 1]
        check.sort(key=lambda x: len(x), reverse=True)
        if not exclude:
            return len(check[0]) if check else -1    
        for s in check:
            is_sub = False
            for e in exclude:
                if subseq(s, e):
                    is_sub = True
                    break
            if not is_sub:
                return len(s)
        return -1