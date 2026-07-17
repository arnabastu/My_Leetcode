class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:  # Fixed: Check for empty inner list
            return False
            
        rows = len(matrix)
        cols = len(matrix[0])           # Fixed: Get actual column count
        
        left = 0
        right = rows * cols - 1
        
        while left <= right:
            mid = left + (right - left) // 2  # Prevents potential overflow
            
            # Convert 1D index to 2D coordinates
            row = mid // cols
            col = mid % cols
            
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False
