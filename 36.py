#36 valid-sudoku/ 
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows=[[False for i in range(0,9)] for j in range(0,9)]
        cols=[[False for i in range(0,9)] for j in range(0,9)]
        subs=[[False for i in range(0,9)] for j in range(0,9)]
        for i in range(0, len(board)):
            for j in range(0, len(board)):
                val = board[i][j]
                if val == '.':
                    continue
                else:
                    val = ord(board[i][j]) - ord('1')
                    if rows[i][val] or cols[j][val] or subs[(i/3)*3+j/3][val]:
                        return False
                    else:
                        rows[i][val] = cols[j][val] = subs[(i/3)*3+j/3][val] = True
        return True
