from typing import List
from collections import deque

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)

        graph = [[] for _ in range(n)]
        indeg = [0] * n

        for u, v, w in edges:
            graph[u].append((v, w))
            indeg[v] += 1

        q = deque(i for i in range(n) if indeg[i] == 0)
        topo = []

        while q:
            u = q.popleft()
            topo.append(u)
            for v, _ in graph[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        INF = 10**30

        def check(limit):
            dist = [INF] * n
            dist[0] = 0

            for u in topo:
                if dist[u] == INF:
                    continue
                if u and u != n - 1 and not online[u]:
                    continue

                for v, w in graph[u]:
                    if w < limit:
                        continue
                    if v != n - 1 and not online[v]:
                        continue

                    nd = dist[u] + w
                    if nd < dist[v]:
                        dist[v] = nd

            return dist[-1] <= k

        if not check(0):
            return -1

        lo, hi = 0, 10**9
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if check(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo