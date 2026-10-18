class Solution:

    def binSearch(self, nums, l, r):
        mid = (l + r) // 2
        val = nums[mid]

        if mid == l:
            return min(nums[l], nums[r])

        if val < nums[l] and val < nums[r]:
            return self.binSearch(nums, l, mid)
        elif val > nums[l] and val > nums[r]:
            return self.binSearch(nums, mid + 1, r)
        else:
            return nums[l]
    def findMin(self, nums: List[int]) -> int:
        return self.binSearch(nums, 0, len(nums) - 1)