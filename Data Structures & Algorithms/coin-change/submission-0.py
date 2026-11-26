class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memory = {}
        #memory[i] entails the min number of coins needed to make up i

        #the problem can be split into three subproblems: min number of coins needed to make up i - coin[0], i - coin[1]...
        def dp(i):

            if i == 0:
                return 0
            if i < 0:
                return float("inf")
            if i in memory:
                return memory[i]
            
            minnum = float("inf")
            for coin in coins:
                still_need = i - coin
                total = 1 + dp(still_need)
                minnum = min(minnum, total)
            
            memory[i] = minnum
            return memory[i]
        
        res = dp(amount)
        return res if res < float("inf") else -1