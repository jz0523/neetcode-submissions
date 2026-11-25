class Solution:
    def rob(self, nums: List[int]) -> int:
        nums1 = nums[:-1]
        nums2 = nums[1:]

        if len(nums) == 1:
            return nums[0]

        def rob_helper(nums):
            memory = {}

            def dp(i):
                if i in memory:
                    return memory[i]
                
                if i == 0:
                    memory[i] = 0
                    return memory[i]
                
                if i == 1:
                    memory[i] = nums[i-1]
                    return memory[i]
                
                memory[i] = max(
                    dp(i-1), dp(i-2) + nums[i-1]
                )
                return memory[i]
            
            return dp(len(nums))
        
        return max(rob_helper(nums1), rob_helper(nums2))