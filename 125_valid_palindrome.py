class Solution:
    def isPalindrome(self, s: str) -> bool:
        rm = "abcdefghijklmnopqrstuvwxyz0123456789"

        s = s.lower()

        result = ""
        for letter in s:
            if letter in rm:
                result += letter
            else:
                continue

        if result == result[::-1]:
            return True
        
        return False