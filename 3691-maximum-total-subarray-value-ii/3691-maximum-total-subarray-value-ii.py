import collections
from bisect import bisect_right

class Solution:
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        n = len(nums)
        _nums = nums
        
        # Step 1: Binary search for the k-th largest subarray value
        # We find the largest threshold such that at least k subarrays have value >= threshold
        low, high = 0, 10**9
        threshold = 0
        
        while low <= high:
            mid = (low + high) // 2
            if mid == 0:
                threshold = 0
                low = 1
                continue
            
            l_cnt = 0
            curr_l = 0
            qm = collections.deque()
            qn = collections.deque()
            qmp, qmpl, qma = qm.pop, qm.popleft, qm.append
            qnp, qnpl, qna = qn.pop, qn.popleft, qn.append
            
            for r, vr in enumerate(_nums):
                while qm and _nums[qm[-1]] <= vr: qmp()
                qma(r)
                while qn and _nums[qn[-1]] >= vr: qnp()
                qna(r)
                
                while _nums[qm[0]] - _nums[qn[0]] >= mid:
                    curr_l += 1
                    if qm[0] < curr_l: qmpl()
                    if qn[0] < curr_l: qnpl()
                l_cnt += curr_l
                # Optimization: Break early if we already found k subarrays
                if l_cnt >= k:
                    break
            
            if l_cnt >= k:
                threshold = mid
                low = mid + 1
            else:
                high = mid - 1
        
        # Step 2: Sum all values strictly greater than threshold
        target_x = threshold + 1
        q_max, q_min = collections.deque(), collections.deque()
        qma, qmp, qmpl = q_max.append, q_max.pop, q_max.popleft
        qna, qnp, qnpl = q_min.append, q_min.pop, q_min.popleft
        
        max_stack, max_starts = [], []
        min_stack, min_starts = [], []
        
        l, c_plus, s_plus = 0, 0, 0
        for r, v in enumerate(_nums):
            # Count logic for subarrays with value >= threshold + 1
            while q_max and _nums[q_max[-1]] <= v: qmp()
            qma(r)
            while q_min and _nums[q_min[-1]] >= v: qnp()
            qna(r)
            while _nums[q_max[0]] - _nums[q_min[0]] >= target_x:
                l += 1
                if q_max[0] < l: qmpl()
                if q_min[0] < l: qnpl()
            c_plus += l
            
            # Sum logic: Maintain max stack prefix areas
            m_start = r
            while max_stack and max_stack[-1][0] <= v:
                m_start = max_stack.pop()[1]
                max_starts.pop()
            prev_m_area = max_stack[-1][2] if max_stack else 0
            max_stack.append((v, m_start, prev_m_area + (r - m_start + 1) * v))
            max_starts.append(m_start)
            
            # Sum logic: Maintain min stack prefix areas
            mi_start = r
            while min_stack and min_stack[-1][0] >= v:
                mi_start = min_stack.pop()[1]
                min_starts.pop()
            prev_mi_area = min_stack[-1][2] if min_stack else 0
            min_stack.append((v, mi_start, prev_mi_area + (r - mi_start + 1) * v))
            min_starts.append(mi_start)
            
            # Query the area [0, l-1] to get the sum of values ending at r
            L = l - 1
            if L >= 0:
                # Max query
                im = bisect_right(max_starts, L) - 1
                sm_tuple = max_stack[im]
                s_plus += (max_stack[im-1][2] if im > 0 else 0) + (L - sm_tuple[1] + 1) * sm_tuple[0]
                # Min query
                imi = bisect_right(min_starts, L) - 1
                smi_tuple = min_stack[imi]
                s_plus -= (min_stack[imi-1][2] if imi > 0 else 0) + (L - smi_tuple[1] + 1) * smi_tuple[0]
        
        # The total value is the sum of (values > threshold) + remaining subarrays * threshold
        return s_plus + (k - c_plus) * threshold