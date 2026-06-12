from typing import List

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        # n nodes, labeled 1 to n. 
        # n-1 edges in a tree means n = len(edges) + 1
        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # 1. BFS to compute depths and immediate parents
        depth = [-1] * (n + 1)
        parent = [0] * (n + 1)
        depth[1] = 0
        queue = [1]
        
        # Standard iterative BFS for speed and to avoid recursion depth issues
        for u in queue:
            for v in adj[u]:
                if depth[v] == -1:
                    depth[v] = depth[u] + 1
                    parent[v] = u
                    queue.append(v)
                    
        # 2. Binary Lifting for LCA (Lowest Common Ancestor)
        LOG = 17 # 2^17 > 10^5
        up = [parent] # up[0] is immediate parents
        for i in range(1, LOG):
            prev_up = up[-1]
            # up[i][v] = up[i-1][up[i-1][v]]
            curr_up = [prev_up[prev_up[v]] for v in range(n + 1)]
            up.append(curr_up)
            
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            
            # Lift u to same depth as v
            diff = depth[u] - depth[v]
            for i in range(LOG):
                if (diff >> i) & 1:
                    u = up[i][u]
            
            if u == v:
                return u
            
            # Lift both until parents match
            for i in range(LOG - 1, -1, -1):
                if up[i][u] != up[i][v]:
                    u = up[i][u]
                    v = up[i][v]
            return up[0][u]

        # 3. Precompute powers of 2 for fast queries
        MOD = 10**9 + 7
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i-1] * 2) % MOD
            
        # 4. Answer Queries
        results = []
        for u, v in queries:
            if u == v:
                results.append(0)
                continue
            
            lca = get_lca(u, v)
            # Path length L
            L = depth[u] + depth[v] - 2 * depth[lca]
            # Ways to assign weights such that cost is odd is 2^(L-1)
            results.append(pow2[L - 1])
            
        return results