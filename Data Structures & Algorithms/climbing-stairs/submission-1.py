class Solution:
    def climbStairs(self, n: int) -> int:
        track = [0]*(n+1)

        def dp(n):

            if track[n] != 0:
                return track[n]

            if n == 1:
                track[n] = 1
                return track[n]
            if n == 2:
                track[n] = 2
                return track[n]
            
            track[n] = dp(n - 1) + dp(n-2)
            return track[n]
        
        return dp(n)
        
        