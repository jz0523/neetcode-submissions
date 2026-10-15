class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        encounter = set()
        maxcount = 0
        l = 0

        for r in range(len(s)):
            while s[r] in encounter:
                encounter.remove(s[l])
                l += 1
            encounter.add(s[r])
            maxcount = max(maxcount, r - l + 1)
        
        return maxcount
        

