import heapq

class Solution:
    def topKFrequent(self, nums, k):
        heap = []
        frequency = {}

        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        for key in frequency:
            heapq.heappush(heap, (frequency[key], key))
            if len(heap) > k:
                heapq.heappop(heap)
                
        return [node[1] for node in heap]

s = Solution()
print(s.topKFrequent([1], 1))