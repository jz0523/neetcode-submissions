class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, subset = [], []
        i = 0
        nums.sort()

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            #choose the curr elm
            num = nums[i]
            subset.append(num)
            dfs(i + 1)
            subset.pop()

            #skip the same elm
            while i < len(nums) and nums[i] == num:
                i += 1
            
            #start from the new elm
            dfs(i)
        
        dfs(0)

        return res