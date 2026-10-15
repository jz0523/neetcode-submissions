class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(nums, target):
            i = 0
            j = len(nums) - 1
            res = []
            while i < j:
                if nums[i] + nums[j] == target:
                    res.append([-target, nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while nums[i] == nums[i - 1] and i < j:
                        i += 1
                elif nums[i] + nums[j] > target:
                    j -= 1
                else:
                    i += 1
            return res
        nums.sort()
        seen = set()
        n = len(nums)
        output = []

        for i in range(n - 1):

            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            neg = -nums[i]
            result = twoSum(nums[i+1:], neg)
            output = output + result

        return output

