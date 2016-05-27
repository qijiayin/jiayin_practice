# 73set-matrix-zeroes/
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) < 1 :
            return
        fst_row_has_zero = False
        for x in matrix[0]:
            if x == 0:
                fst_row_has_zero = True
                break

        fst_col_has_zero = False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                fst_col_has_zero = True
                break

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0

        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(len(matrix)) :
                    matrix[i][j] = 0

        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(len(matrix[0])) :
                    matrix[i][j] = 0

        if fst_row_has_zero == True:
            for j in range(len(matrix[0])) :
                matrix[0][j] = 0
        if fst_col_has_zero == True:
            for i in range(len(matrix)) :
                matrix[i][0] = 0
