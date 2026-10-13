from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = [[] for i in range(len(nums) + 1)]
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        for num, cnt in count.items():
            arr[cnt].append(num)
        
        res = []
        for i in range(len(arr) - 1, -1, -1):
            for num in arr[i]:
                res.append(num)
                if len(res) == k:
                    return res