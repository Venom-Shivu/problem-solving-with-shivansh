from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        clones = {node: Node(node.val)}
        q = deque([node])

        while q:
            curr = q.popleft()

            clone = clones[curr]

            for nei in curr.neighbors:
                if nei not in clones:
                    clones[nei] = Node(nei.val)
                    q.append(nei)

                clone.neighbors.append(clones[nei])

        return clones[node]