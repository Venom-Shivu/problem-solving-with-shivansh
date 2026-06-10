from bisect import bisect_right
from typing import List

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 0: return 0
        
        # Local variables for hyper-optimized indexing
        q1 = [0] * n
        q1v = [0] * n
        q2 = [0] * n
        q2v = [0] * n
        
        low = 1
        high = 1000000000 # max possible value of nums[i]
        threshold = 0
        
        # Step 1: Binary Search for the k-th largest subarray value
        while low <= high:
            mid = (low + high) >> 1
            l_cnt = 0
            curr_l = 0
            h1 = t1 = h2 = t2 = 0
            
            for r, vr in enumerate(nums):
                # Update monotonic max queue
                while t1 > h1 and q1v[t1 - 1] <= vr:
                    t1 -= 1
                q1[t1] = r
                q1v[t1] = vr
                t1 += 1
                
                # Update monotonic min queue
                while t2 > h2 and q2v[t2 - 1] >= vr:
                    t2 -= 1
                q2[t2] = r
                q2v[t2] = vr
                t2 += 1
                
                v1, v2 = q1v[h1], q2v[h2]
                while v1 - v2 >= mid:
                    curr_l += 1
                    if q1[h1] < curr_l:
                        h1 += 1
                        v1 = q1v[h1]
                    if q2[h2] < curr_l:
                        h2 += 1
                        v2 = q2v[h2]
                l_cnt += curr_l
                if l_cnt >= k:
                    break
            
            if l_cnt >= k:
                threshold = mid
                low = mid + 1
            else:
                high = mid - 1
        
        # Step 2: Final Summation for values strictly greater than threshold
        target_x = threshold + 1
        s_plus = 0
        c_plus = 0
        h1 = t1 = h2 = t2 = 0
        curr_l = 0
        
        max_stack = [] # (val, start_idx, area_prefix_sum)
        max_starts = []
        min_stack = []
        min_starts = []
        
        for r, vr in enumerate(nums):
            while t1 > h1 and q1v[t1 - 1] <= vr: t1 -= 1
            q1[t1] = r; q1v[t1] = vr; t1 += 1
            while t2 > h2 and q2v[t2 - 1] >= vr: t2 -= 1
            q2[t2] = r; q2v[t2] = vr; t2 += 1
            
            v1, v2 = q1v[h1], q2v[h2]
            while v1 - v2 >= target_x:
                curr_l += 1
                if q1[h1] < curr_l:
                    h1 += 1
                    v1 = q1v[h1]
                if q2[h2] < curr_l:
                    h2 += 1
                    v2 = q2v[h2]
            c_plus += curr_l
            
            # Monotonic Stack for Max Contribution
            m_start = r
            while max_stack and max_stack[-1][0] <= vr:
                m_start = max_stack.pop()[1]
                max_starts.pop()
            prev_area = max_stack[-1][2] if max_stack else 0
            max_stack.append((vr, m_start, prev_area + (r - m_start + 1) * vr))
            max_starts.append(m_start)
            
            # Monotonic Stack for Min Contribution
            mi_start = r
            while min_stack and min_stack[-1][0] >= vr:
                mi_start = min_stack.pop()[1]
                min_starts.pop()
            prev_area_mi = min_stack[-1][2] if min_stack else 0
            min_stack.append((vr, mi_start, prev_area_mi + (r - mi_start + 1) * vr))
            min_starts.append(mi_start)
            
            L = curr_l - 1
            if L >= 0:
                # Query sum of Max and Min for all starts l in [0, L]
                idx = bisect_right(max_starts, L) - 1
                s_plus += (max_stack[idx-1][2] if idx > 0 else 0) + (L - max_stack[idx][1] + 1) * max_stack[idx][0]
                
                idx_mi = bisect_right(min_starts, L) - 1
                s_plus -= (min_stack[idx_mi-1][2] if idx_mi > 0 else 0) + (L - min_stack[idx_mi][1] + 1) * min_stack[idx_mi][0]
                
        return s_plus + (k - c_plus) * threshold