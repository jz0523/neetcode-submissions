class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = [char.lower() for char in s if char.isalnum()]
        letters_only = "".join(letters)

        i = 0
        j = len(letters_only) - 1

        while i < j:
            if letters_only[i] == letters_only[j]:
               i += 1
               j -= 1
            else:
                return False
        
        return True