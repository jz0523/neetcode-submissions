class Solution:
    def binSearch(self, l, r, nums, target):
        if l > r:
            return -1
        m = (l + r) // 2

        if nums[m] == target:
            return m
        elif nums[m] < target:
            return self.binSearch(m + 1, r, nums, target)
        else:
            return self.binSearch(l, m - 1, nums, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.binSearch(0, len(nums) - 1, nums, target)
        
        
        
            