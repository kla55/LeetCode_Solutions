class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_opp = str(x)[::-1]
        if str(x) == str(x_opp):
            return True
        else: 
            return False
        