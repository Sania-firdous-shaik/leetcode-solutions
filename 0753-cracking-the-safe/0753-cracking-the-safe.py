class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        if n == 1:
            return "".join(map(str, range(k)))
        seen, res = set(), []
        node = "0" * (n - 1)
        self.dfs(node, k, seen, res)
        return "".join(res) + node
    def dfs(self, node, k, seen, res):
        for i in range(k):
            nxt = node + str(i)
            if nxt not in seen:
                seen.add(nxt)
                self.dfs(nxt[1:], k, seen, res)
                res.append(str(i))