class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        l_cnt = min(m // 2, n // 2)
        for l in range(l_cnt):
            r, c, v = [], [], []
            for i in range(l, m - l - 1):
                r.append(i); c.append(l); v.append(grid[i][l])
            for j in range(l, n - l - 1):
                r.append(m - l - 1); c.append(j); v.append(grid[m - l - 1][j])
            for i in range(m - l - 1, l, -1):
                r.append(i); c.append(n - l - 1); v.append(grid[i][n - l - 1])
            for j in range(n - l - 1, l, -1):
                r.append(l); c.append(j); v.append(grid[l][j])
            tot = len(v)
            rot = k % tot
            for i in range(tot):
                idx = (i + tot - rot) % tot
                grid[r[i]][c[i]] = v[idx]
        return grid