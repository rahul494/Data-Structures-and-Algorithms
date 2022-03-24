def merge_intervals(intervals):

    intervals.sort(key = lambda x: x[0])

    merged = [intervals[0]]

    for i in range(1, len(intervals)):
        latest = merged[-1][1]
        start = intervals[i][0]
        end = intervals[i][1]
        
        if latest >= start and latest < end:
            merged[-1][1] = end
        else:
            merged.append(intervals[i])

    return merged

print(merge_intervals([[1,4], [2,6], [8,10]]))