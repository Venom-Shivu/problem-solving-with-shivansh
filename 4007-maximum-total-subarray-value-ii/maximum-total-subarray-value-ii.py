import collections
from bisect import bisect_right

class Solution:
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        n = len(nums)

        def count(X):
            """Counts the number of subarrays with value (max - min) >= X."""
            if X <= 0:
                return n * (n + 1) // 2
            l = 0
            cnt = 0
            max_q = collections.deque()
            min_q = collections.deque()
            for r in range(n):
                while max_q and nums[max_q[-1]] <= nums[r]:
                    max_q.pop()
                max_q.append(r)
                while min_q and nums[min_q[-1]] >= nums[r]:
                    min_q.pop()
                min_q.append(r)
                
                # As l increases, V(l, r) is non-increasing. 
                # We find the largest l such that V(l, r) >= X.
                while max_q and min_q and nums[max_q[0]] - nums[min_q[0]] >= X:
                    l += 1
                    if max_q[0] < l:
                        max_q.popleft()
                    if min_q[0] < l:
                        min_q.popleft()
                cnt += l
            return cnt

        def sum_of_values_ge(X):
            """Calculates the sum of values (max - min) for all subarrays with value >= X."""
            if X <= 0:
                return 0
            l = 0
            L_array = [-1] * n
            max_q = collections.deque()
            min_q = collections.deque()
            # First pass: find the boundary L for each r
            for r in range(n):
                while max_q and nums[max_q[-1]] <= nums[r]:
                    max_q.pop()
                max_q.append(r)
                while min_q and nums[min_q[-1]] >= nums[r]:
                    min_q.pop()
                min_q.append(r)
                while max_q and min_q and nums[max_q[0]] - nums[min_q[0]] >= X:
                    l += 1
                    if max_q[0] < l:
                        max_q.popleft()
                    if min_q[0] < l:
                        min_q.popleft()
                L_array[r] = l - 1

            total_max_sum = 0
            total_min_sum = 0
            # Stack elements: [start_index, value, cumulative_area_sum]
            # cumulative_area_sum represents sum of max(i, r) for i in [0, r]
            max_stack = [] 
            min_stack = []
            
            for r in range(n):
                # Update Max Stack
                m_idx = r
                while max_stack and max_stack[-1][1] <= nums[r]:
                    m_idx = max_stack.pop()[0]
                prev_total_max = max_stack[-1][2] if max_stack else 0
                max_stack.append([m_idx, nums[r], prev_total_max + (r - m_idx + 1) * nums[r]])

                # Update Min Stack
                mi_idx = r
                while min_stack and min_stack[-1][1] >= nums[r]:
                    mi_idx = min_stack.pop()[0]
                prev_total_min = min_stack[-1][2] if min_stack else 0
                min_stack.append([mi_idx, nums[r], prev_total_min + (r - mi_idx + 1) * nums[r]])

                L = L_array[r]
                if L >= 0:
                    # Query sum of max(i, r) for i in [0, L]
                    p_m = bisect_right(max_stack, L, key=lambda x: x[0]) - 1
                    base_max = max_stack[p_m-1][2] if p_m > 0 else 0
                    total_max_sum += base_max + (L - max_stack[p_m][0] + 1) * max_stack[p_m][1]

                    # Query sum of min(i, r) for i in [0, L]
                    p_mi = bisect_right(min_stack, L, key=lambda x: x[0]) - 1
                    base_min = min_stack[p_mi-1][2] if p_mi > 0 else 0
                    total_min_sum += base_min + (L - min_stack[p_mi][0] + 1) * min_stack[p_mi][1]

            return total_max_sum - total_min_sum

        # Step 1: Binary search for the k-th largest subarray value
        low, high = 0, 10**9
        threshold = 0
        while low <= high:
            mid = (low + high) // 2
            if count(mid) >= k:
                threshold = mid
                low = mid + 1
            else:
                high = mid - 1
        
        # Step 2: Sum top k values
        c_plus = count(threshold + 1)
        s_plus = sum_of_values_ge(threshold + 1)
        return s_plus + (k - c_plus) * threshold