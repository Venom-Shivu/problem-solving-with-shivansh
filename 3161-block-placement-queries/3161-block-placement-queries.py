from typing import List
from sortedcontainers import SortedDict


class Obstacle:
    """
    Doubly linked list node.

    Used for:
    1. Obstacle positions
    2. Prefix maximum-gap checkpoints
    """

    def __init__(self, x: int, max_gap: int, previous):
        self.x = x
        self.max_gap = max_gap

        self.previous = previous
        self.next = None

    def remove(self):
        """
        Remove current node from linked list.
        Returns next node.
        """
        if self.previous:
            self.previous.next = self.next

        if self.next:
            self.next.previous = self.previous

        return self.next


class Solution:

    # ---------------------------------------------------------
    # Query Type 2
    # ---------------------------------------------------------

    def can_place(
        self,
        obstacle_tree: SortedDict,
        max_gap_tree: SortedDict,
        x: int,
        size: int
    ) -> bool:

        # Find largest prefix max-gap before x
        gap_key = next(
            max_gap_tree.irange(maximum=x, reverse=True),
            None
        )

        gap_node = max_gap_tree[gap_key]

        if gap_node.max_gap >= size:
            return True

        # Check last segment ending at x
        obstacle_key = next(
            obstacle_tree.irange(maximum=x, reverse=True),
            None
        )

        obstacle = obstacle_tree[obstacle_key]

        return (x - obstacle.x) >= size

    # ---------------------------------------------------------
    # Reverse obstacle insertion
    # ---------------------------------------------------------

    def remove_obstacle(
        self,
        obstacle_tree: SortedDict,
        max_gap_tree: SortedDict,
        x: int
    ):

        obstacle_to_remove = obstacle_tree.pop(x)

        next_obstacle = obstacle_to_remove.remove()

        # Remove corresponding max-gap node if it exists
        removed_gap_node = max_gap_tree.pop(x, None)

        if removed_gap_node is not None:
            removed_gap_node.remove()

        if next_obstacle is None:
            return

        # New merged gap after removing obstacle
        merged_gap = (
            next_obstacle.x -
            next_obstacle.previous.x
        )

        gap_position = next_obstacle.x

        prev_gap_key = next(
            max_gap_tree.irange(maximum=x, reverse=True),
            None
        )

        prev_gap_node = max_gap_tree[prev_gap_key]

        # Nothing changes if previous max gap is already larger
        if prev_gap_node.max_gap >= merged_gap:
            return

        current = prev_gap_node.next

        # Remove dominated max-gap nodes
        while current and current.max_gap <= merged_gap:

            nxt = current.next

            max_gap_tree.pop(current.x, None)

            current.remove()

            current = nxt

        # Insert new max-gap checkpoint
        new_node = Obstacle(
            gap_position,
            merged_gap,
            prev_gap_node
        )

        prev_gap_node.next = new_node
        new_node.next = current

        if current:
            current.previous = new_node

        max_gap_tree[new_node.x] = new_node

    # ---------------------------------------------------------
    # Main
    # ---------------------------------------------------------

    def getResults(self, queries: List[List[int]]) -> List[bool]:

        obstacle_positions = []

        for query in queries:
            if query[0] == 1:
                obstacle_positions.append(query[1])

        obstacle_positions.sort()

        # -------------------------------------------------
        # Obstacle linked list
        # -------------------------------------------------

        obstacle_head = Obstacle(0, 0, None)

        obstacle_tree = SortedDict()
        obstacle_tree[0] = obstacle_head

        current_obstacle = obstacle_head

        # -------------------------------------------------
        # Max-gap linked list
        # -------------------------------------------------

        gap_head = Obstacle(0, 0, None)

        max_gap_tree = SortedDict()
        max_gap_tree[0] = gap_head

        current_gap = gap_head

        max_gap_so_far = 0

        # -------------------------------------------------
        # Build structures
        # -------------------------------------------------

        for pos in obstacle_positions:

            gap = pos - current_obstacle.x

            if gap > max_gap_so_far:

                max_gap_so_far = gap

                gap_node = Obstacle(
                    pos,
                    max_gap_so_far,
                    current_gap
                )

                current_gap.next = gap_node
                current_gap = gap_node

                max_gap_tree[pos] = gap_node

            obstacle_node = Obstacle(
                pos,
                max_gap_so_far,
                current_obstacle
            )

            current_obstacle.next = obstacle_node
            current_obstacle = obstacle_node

            obstacle_tree[pos] = obstacle_node

        # -------------------------------------------------
        # Process queries in reverse
        # -------------------------------------------------

        answers = []

        for query in reversed(queries):

            if query[0] == 1:

                self.remove_obstacle(
                    obstacle_tree,
                    max_gap_tree,
                    query[1]
                )

            else:

                answers.append(
                    self.can_place(
                        obstacle_tree,
                        max_gap_tree,
                        query[1],
                        query[2]
                    )
                )

        answers.reverse()

        return answers