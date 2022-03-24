import collections

def merge_intervals(intervals):

    intervals.sort(key = lambda x: x[0])

    merged = [intervals[0]]

    for i in range(1, len(intervals) + 1):
        start, end = intervals[i]
        print(start)
        print(end)

merge_intervals([[1,4], [2,6], [8,10]])