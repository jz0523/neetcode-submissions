class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        vocab = set()
        for word in wordDict:
            vocab.add(word)
        
        memory = {}
        #memory[i] stores binary, indicating whether the first i elements can be split

        def dp(i):
            
            if i == 0:
                memory[i] = True
                return True

            if i in memory:
                return memory[i]

            for idx in range(i - 1, -1, -1):
                currstr = s[idx:i]
                if currstr not in vocab:
                    continue
                else:
                    if dp(idx):
                        memory[i] = True
                        return memory[i]
            
            memory[i] = False
            return memory[i]
        
        return dp(len(s))
                
