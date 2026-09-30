from collections import defaultdict
from typing import List
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (u, v), val in zip(equations, values):
            graph[u][v] = val
            graph[v][u] = 1.0 / val

        def dfs(curr: str, target: str, visited: set) -> float:
            if curr not in graph or target not in graph:
                return -1.0
            if curr == target:
                return 1.0
            visited.add(curr)
            for nxt, weight in graph[curr].items():
                if nxt not in visited:
                    res = dfs(nxt, target, visited)
                    if res != -1.0:
                        return res * weight
            return -1.0
        return [dfs(src, dst, set()) for src, dst in queries]