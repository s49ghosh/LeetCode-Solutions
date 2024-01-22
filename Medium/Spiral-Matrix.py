class Solution:

    # Start top, bottom, left, right at ends of matrix and slowly bring them toward the middle
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # If matrix is empty, return empty list
        if not matrix:
            return []

        rows, cols = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, rows-1, 0, cols-1
        result = []
        
        # Length of output array will be rows * cols
        while len(result) < rows * cols:
            # Go left to right first, increment top to record we finished the top row
            for i in range(left, right+1):
                result.append(matrix[top][i])
            top += 1
            
            # Go top to bottom, decrement right to record we finished the right column
            for i in range(top, bottom+1):
                result.append(matrix[i][right])
            right -= 1
            
            # If there are still rows to traverse
            if top <= bottom:
                # Go right to left, decrement bottom to record we finished the bottom row
                for i in range(right, left-1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            
            # If there are still columns to traverse
            if left <= right:
                # Go bottom to top, increment left to record we finished the left column
                for i in range(bottom, top-1, -1):
                    result.append(matrix[i][left])
                left += 1
        
        return result