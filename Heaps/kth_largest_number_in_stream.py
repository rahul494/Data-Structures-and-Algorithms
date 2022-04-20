from heapq import *

def kth_largest_number_in_stream(nums, k):
    min_heap = []
    for num in nums:
        heappush(min_heap, num)
        if len(min_heap) > k:
            heappop(min_heap)

    return min_heap[0]    
    

print(kth_largest_number_in_stream([3, 1, 5, 12, 2, 11], 4))
print(kth_largest_number_in_stream([3, 1, 5, 12, 2, 11, 6], 4))
print(kth_largest_number_in_stream([3, 1, 5, 12, 2, 11, 6, 13], 4))
print(kth_largest_number_in_stream([3, 1, 5, 12, 2, 11, 6, 13, 4], 4))