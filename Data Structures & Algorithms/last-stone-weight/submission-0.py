class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # want to use max-heap
        heapq.heapify_max(stones)

        while len(stones)>=2:
            big = heapq.heappop_max(stones)
            small = heapq.heappop_max(stones)
            if big !=small: 
                heapq.heappush_max(stones, big-small)
        if len(stones)==0: return 0
        return stones[0]