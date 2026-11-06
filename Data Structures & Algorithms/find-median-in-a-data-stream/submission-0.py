import heapq
class MedianFinder:

#maintain two heap, smallhald which is a maxheap, and bighalf which is a minheap

    def __init__(self):
        self.smallhalf = []
        self.bighalf = []
        self.even = True

    def addNum(self, num: int) -> None:
        if not self.smallhalf and not self.bighalf:
            heapq.heappush_max(self.smallhalf, num)
        elif num > self.smallhalf[0]:
            heapq.heappush(self.bighalf, num)
            if len(self.bighalf) > 1 + len(self.smallhalf):
                heapq.heappush_max(self.smallhalf, heapq.heappop(self.bighalf))
        else:
            heapq.heappush_max(self.smallhalf, num)
            if len(self.smallhalf) > 1 + len(self.bighalf):
                heapq.heappush(self.bighalf, heapq.heappop_max(self.smallhalf))
        
        self.even = not self.even


    def findMedian(self) -> float:

        if len(self.smallhalf) > len(self.bighalf):
            return self.smallhalf[0]
        elif len(self.smallhalf) < len(self.bighalf):
            return self.bighalf[0]
        else:
            return (self.smallhalf[0] + self.bighalf[0]) / 2
        