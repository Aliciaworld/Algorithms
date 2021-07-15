class Solution:
    def reverseString(self, s:list[str]):
        left = 0
        right = len(s) - 1
        while left < right:
            hold = s[left]
            s[left] = s[right]
            s[right] = hold
            left += 1
            right -= 1

