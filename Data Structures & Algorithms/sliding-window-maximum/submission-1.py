import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))

            if i >= k - 1 and i < len(nums):
                while heap[0][1] < i - k + 1:
                    heapq.heappop(heap)
                maxval = -heap[0][0]
                res.append(maxval)

        return res