https://leetcode.com/problems/single-number/
    

class Solution(object):
    def singleNumber(self, nums):
        ans = 0
        for num in nums:
            ans ^= num
        return ans
    
