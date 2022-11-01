import heapq

def topKFrequent(nums, k):

    print(nums)
    heapq.heapify(nums)
    print(nums)

topKFrequent([1,1,1,2,2,3], 2)

