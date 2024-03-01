class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = ((str(x)[::-1]))
        if x < 0:
            return False
        elif x == int(y):
            return True
        else:
            return False

