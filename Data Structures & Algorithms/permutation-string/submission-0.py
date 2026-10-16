class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0]*26, [0]*26
        for c in s1:
            s1Count[ord(c) - ord('a')] += 1
        
        l = 0

        for r in range(len(s2)):
            c = s2[r]
            if s1Count[ord(c) - ord('a')] == 0:
                l = r + 1
                count = 0
                s2Count = [0]*26
                continue
            
            s2Count[ord(c) - ord('a')] += 1

            while s2Count[ord(c) - ord('a')] > s1Count[ord(c) - ord('a')]:
                s2Count[ord(s2[l]) - ord('a')] -= 1
                l += 1
            
            if r - l + 1 == len(s1):
                return True
        
        return False


