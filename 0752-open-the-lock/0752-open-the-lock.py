from collections import deque
from typing import List
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visi = set(deadends)
        if "0000" in visi or target in visi:
            return -1
        q = deque([("0000", 0)])
        visi.add("0000")
        while q:
            curr, d = q.popleft()
            if curr == target:
                return d
            for i in range(4):
                for j in [-1, 1]:
                    new = curr[:i] + str((int(curr[i]) + j) % 10) + curr[i+1:]
                    if new not in visi:
                        q.append((new, d + 1))
                        visi.add(new)
        return -1