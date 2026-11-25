class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memory = {}
        #define the memory[i] (the state) as the max money we can rob in the first i houses in total. The TLQ is: are we gonna rob this house or no

        def dp(i):

            if i in memory:
                return memory[i]

            if i == 0:
                memory[i] = 0
                return 0

            if i == 1:
                memory[i] = nums[i-1]
                return memory[i]
            
            memory[i] = max(
                dp(i-1), dp(i-2) + nums[i-1]
            )

            return memory[i]
        
        return dp(len(nums))