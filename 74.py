#74 search-a-2d-matrix/
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if len(matrix) < 1:
            return False

        m = len(matrix)
        n = len(matrix[0])
        beg_row = 0
        end_row = m - 1
        while beg_row <= end_row :
            mid_row = (beg_row + end_row) / 2
            if target >= matrix[mid_row][0] and target <= matrix[mid_row][n-1]:
                beg_col = 0
                end_col = n - 1
                while beg_col <= end_col:
                    mid_col = (beg_col + end_col )/2
                    val =  matrix[mid_row][mid_col]
                    if val == target :
                        return True
                    else:
                        if val > target:
                            end_col = mid_col - 1
                        if val < target:
                            beg_col = mid_col + 1
                return False

            else:
                if  target < matrix[mid_row][0] :
                    end_row = mid_row - 1
                if target > matrix[mid_row][n-1] :
                    beg_row = mid_row + 1

        return False
