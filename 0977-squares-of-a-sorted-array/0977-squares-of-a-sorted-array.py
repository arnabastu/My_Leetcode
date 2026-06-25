class Solution(object):
    def sortedSquares(self, nums):
        square = [num * num for num in nums]
        return sorted(square)
        

        