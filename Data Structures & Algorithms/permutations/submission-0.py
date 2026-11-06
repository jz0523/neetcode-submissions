class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, curr = [], []
        i = 0
        chosen = [False for i in range(len(nums))]

        def dfs():
            if len(curr) == len(nums):
                res.append(curr.copy())
            
            for j in range(len(nums)):
                if chosen[j]:
                    continue
                #choose the elm
                curr.append(nums[j])
                chosen[j] = True
                dfs()

                curr.pop()
                chosen[j] = False


        dfs()
    
        return res
