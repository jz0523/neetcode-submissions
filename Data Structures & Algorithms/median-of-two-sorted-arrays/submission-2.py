class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        lenTotal = len(A) + len(B)
        mid = lenTotal // 2

        if len(A) > len(B):
            A, B = B, A
        
        lenA = len(A)
        lenB = len(B)
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = mid - (i + 1) - 1

            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if (i+1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if (j+1) < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if lenTotal % 2:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

