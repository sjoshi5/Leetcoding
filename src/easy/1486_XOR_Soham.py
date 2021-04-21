class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        cur=start
        for i in range(1,n):
            cur = cur^(start+2*i)
        return cur

#Time complexity O(n): Iterate only once
#Space Complexity: O(1): No need to store the array