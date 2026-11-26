class Solution:
    def numDecodings(self, s: str) -> int:
        count = 0
        memory = {}
        #TLQ: should the last digit be decoded as is, or combined with its previous one to form two digits? 
        #memory[i] entails the total number of ways to decode the first i elements.

        def dp(i):
            if i in memory:
                return memory[i]
            
            if i == 0:
                return 1
            
            ways = 0
            dig = s[i-1]
            if dig != "0":
                ways += dp(i-1)
            
            if i >= 2 and 10 <= int(s[i-2:i]) <= 26:
                ways += dp(i-2)
            
            memory[i] = ways

            return memory[i]
        
        return dp(len(s))

