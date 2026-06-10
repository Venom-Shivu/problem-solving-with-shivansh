from typing import List

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 0: return 0
        
        # Pre-allocate for monotonic queues
        # Use simple lists and manual head/tail pointers for speed
        q1 = [0] * n   # indices for max
        q1v = [0] * n  # values for max
        q2 = [0] * n   # indices for min
        q2v = [0] * n  # values for min
        
        # Binary search for threshold X
        low = 1
        high = max(nums) - min(nums)
        threshold = 0
        
        # Optimize loop: Local variable lookups are faster than list lookups
        while low <= high:
            mid = (low + high) >> 1
            h1 = t1 = h2 = t2 = 0
            curr_l = 0
            l_cnt = 0
            
            for r in range(n):
                vr = nums[r]
                # Inline monotonic queue updates
                while t1 > h1 and q1v[t1 - 1] <= vr: t1 -= 1
                q1[t1] = r; q1v[t1] = vr; t1 += 1
                
                while t2 > h2 and q2v[t2 - 1] >= vr: t2 -= 1
                q2[t2] = r; q2v[t2] = vr; t2 += 1
                
                # Check condition and update l-pointer
                v1, v2 = q1v[h1], q2v[h2]
                if v1 - v2 >= mid:
                    while v1 - v2 >= mid:
                        curr_l += 1
                        if q1[h1] < curr_l:
                            h1 += 1
                            v1 = q1v[h1]
                        if q2[h2] < curr_l:
                            h2 += 1
                            v2 = q2v[h2]
                l_cnt += curr_l
                if l_cnt >= k: break # Critical optimization
            
            if l_cnt >= k:
                threshold = mid
                low = mid + 1
            else:
                high = mid - 1
                
        # Final pass: $O(N)$ summation
        # We replace bisect_right with a moving pointer since L is non-decreasing
        target_x = threshold + 1
        s_plus = c_plus = curr_l = h1 = t1 = h2 = t2 = 0
        
        # Stack elements: [value, start_index, cumulative_area]
        # Using separate lists for stack components to speed up indexing
        max_s_v, max_s_i, max_s_a = [], [], []
        min_s_v, min_s_i, min_s_a = [], [], []
        p_max = p_min = 0 # Moving pointers for summation
        
        for r in range(n):
            vr = nums[r]
            while t1 > h1 and q1v[t1 - 1] <= vr: t1 -= 1
            q1[t1] = r; q1v[t1] = vr; t1 += 1
            while t2 > h2 and q2v[t2 - 1] >= vr: t2 -= 1
            q2[t2] = r; q2v[t2] = vr; t2 += 1
            
            v1, v2 = q1v[h1], q2v[h2]
            if v1 - v2 >= target_x:
                while v1 - v2 >= target_x:
                    curr_l += 1
                    if q1[h1] < curr_l: h1 += 1; v1 = q1v[h1]
                    if q2[h2] < curr_l: h2 += 1; v2 = q2v[h2]
            c_plus += curr_l
            
            # Update Max Stack
            m_start = r
            while max_s_v and max_s_v[-1] <= vr:
                max_s_v.pop(); max_s_a.pop()
                m_start = max_s_i.pop()
            prev_a = max_s_a[-1] if max_s_a else 0
            max_s_v.append(vr); max_s_i.append(m_start); max_s_a.append(prev_a + (r - m_start + 1) * vr)
            
            # Update Min Stack
            mi_start = r
            while min_s_v and min_s_v[-1] >= vr:
                min_s_v.pop(); min_s_a.pop()
                mi_start = min_s_i.pop()
            prev_ai = min_s_a[-1] if min_s_a else 0
            min_s_v.append(vr); min_s_i.append(mi_start); min_s_a.append(prev_ai + (r - mi_start + 1) * vr)
            
            # O(N) query using moving pointer for L = curr_l - 1
            L = curr_l - 1
            if L >= 0:
                # Max Contribution
                if p_max >= len(max_s_i): p_max = len(max_s_i) - 1
                while p_max + 1 < len(max_s_i) and max_s_i[p_max + 1] <= L: p_max += 1
                while p_max > 0 and max_s_i[p_max] > L: p_max -= 1
                s_plus += (max_s_a[p_max-1] if p_max > 0 else 0) + (L - max_s_i[p_max] + 1) * max_s_v[p_max]
                
                # Min Contribution
                if p_min >= len(min_s_i): p_min = len(min_s_i) - 1
                while p_min + 1 < len(min_s_i) and min_s_i[p_min + 1] <= L: p_min += 1
                while p_min > 0 and min_s_i[p_min] > L: p_min -= 1
                s_plus -= (min_s_a[p_min-1] if p_min > 0 else 0) + (L - min_s_i[p_min] + 1) * min_s_v[p_min]

        return s_plus + (k - c_plus) * threshold