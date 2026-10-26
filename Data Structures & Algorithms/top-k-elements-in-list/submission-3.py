class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for x in nums:
            count[x] = 1 + count.get(x, 0)
        
        heap = []
        for num in count.keys():
            heapq.heappush(heap, [count[num], num])
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        while len(heap) != 0:
            res.append(heapq.heappop(heap)[1])
        return res