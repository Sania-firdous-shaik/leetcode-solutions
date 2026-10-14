class Solution:
    def minJumps(self, a: List[int]) -> int:
        n = len(a)
        d = [-1] * n
        d[0] = 0
        o = defaultdict(list)
        for i, x in enumerate(a): o[x].append(i)
        q = deque(o[a[0]])
        while q:
            i = q.popleft()
            if i and d[i-1] == -1:
                d[i-1] = d[i] + 1
                q.append(i-1)
            if i+1 < n and d[i+1] == -1:
                d[i+1] = d[i] + 1
                q.append(i+1)
            for j in o[a[i]]:
                if d[j] == -1:
                    d[j] = d[i] + 1
                    q.append(j)
            o[a[i]] = []
        return d[-1]