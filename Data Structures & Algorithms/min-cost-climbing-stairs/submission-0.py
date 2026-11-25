class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memory = {}
        # def memory[i] to be the min cost to reach step i

        def dp(i):

            if i in memory:
                return memory[i]

            if i <= 1:
                memory[i] = 0
                return 0
            
            memory[i] = min(dp(i-1) + cost[i-1], dp(i-2) + cost[i-2])
            
            return memory[i]
        
        return dp(len(cost))
        