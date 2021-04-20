class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        return len([y for y in nums if len(str(y))%2==0])

# Return length of [list of { numbers with even length}]