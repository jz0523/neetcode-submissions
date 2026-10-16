import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        numInterval = len(nums) - k + 1

        l = 0 # l = r - k + 1
        r = k - 1
        res = [0]*numInterval
        sublist = []
        for i in range(k):
            pair = (-nums[i], i)
            sublist.append(pair)

        heapq.heapify(sublist)
        heap = sublist

        for i in range(numInterval):
            if r < len(nums) and r >= k:
                heapq.heappush(heap, (-nums[r], r))

            while heap[0][1] < l:
                heapq.heappop(heap)
            
            maxpair = heap[0]
            res[i] = -maxpair[0]
            r += 1
            l += 1

        return res