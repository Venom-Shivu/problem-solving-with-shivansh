class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        merged_list = []
        curr_pair = intervals[0]

        for start, end in intervals:
            if start > curr_pair[1]:
                merged_list.append(curr_pair)
                curr_pair = [start, end]
            elif end > curr_pair[1]:
                curr_pair[1] = end
        
        merged_list.append(curr_pair)
        return merged_list