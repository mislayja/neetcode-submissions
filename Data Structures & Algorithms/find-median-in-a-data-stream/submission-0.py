class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.small, num)

        # ensure every element in small is <= elements in large. 
        if (self.small and self.large and self.small[0]> self.large[0]):
            # move the item over
            heapq.heappush(self.large, heapq.heappop_max(self.small))
        
        if len(self.small) > len(self.large)+1:
            heapq.heappush(self.large, heapq.heappop_max(self.small))
        if len(self.large) > len(self.small)+1:
            # remove form large add to small
            heapq.heappush_max(self.small, heapq.heappop(self.large))


    def findMedian(self) -> float:
        if len(self.small)==len(self.large):
            return (self.small[0]+self.large[0])/2
        elif len(self.small)> len(self.large):
            return self.small[0]
        else: 
            return self.large[0]
        
        