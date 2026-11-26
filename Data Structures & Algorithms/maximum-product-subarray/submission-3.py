class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currmin = currmax = globalmax = nums[0]
        # memory[i] stores the min and max of substrings ending at the ith num.
        for x in nums[1:]:
            #three cases: start a new substring, multiple with prev min, multiple with prev max
            case1 = x
            case2 = currmin * x
            case3 = currmax * x

            currmax = max(case1, case2, case3)
            currmin = min(case1, case2, case3)
            globalmax = max(globalmax, currmax)
        
        return globalmax

