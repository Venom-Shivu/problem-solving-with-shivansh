class Solution:
    def merge(self, intervals):

        intervals.sort()

        res = []
        append = res.append

        cur_start, cur_end = intervals[0]

        for start, end in intervals[1:]:

            if start <= cur_end:

                if end > cur_end:
                    cur_end = end

            else:

                append([cur_start, cur_end])

                cur_start = start
                cur_end = end

        append([cur_start, cur_end])

        return res