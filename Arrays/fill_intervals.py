def fill_intervals(intervals, new_interval):
    
    # intervals.sort(key = lambda x: x[0])
    merged = []
    i, start, end = 0, 0, 1
    
    # skip/add elements we dont need to merge with the new interval
    # stop looping when there is an overlap intervals[i][end] < new_interval[start]
    while i < len(intervals) and intervals[i][end] < new_interval[start]:
        merged.append(intervals[i])
        i += 1

    while i < len(intervals) and intervals[i][start] <= new_interval[end]:
        new_interval[start] = min(intervals[i][start], new_interval[start])
        new_interval[end] = max(new_interval[end], intervals[i][end])
        i += 1
    
    merged.append(new_interval)

    while i < len(intervals):
        merged.append(intervals[i])
        i += 1
    
    return merged

print(fill_intervals([[1,3], [5,7], [8,12]], [4,6])) # [[1,3], [4,7], [8,12]]
print(fill_intervals([[1,3], [5,7], [8,12]], [4,10])) # [[1,3],[4,12]]
print(fill_intervals([[2,3], [5,7]], [1,4])) # [[1,4], [5,7]]