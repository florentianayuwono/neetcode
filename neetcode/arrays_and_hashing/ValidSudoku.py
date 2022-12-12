class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colMap = dict()
        rowMap = dict()
        boxMap = dict()
        for i in range(len(board)):
            rowMap[i] = set()
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                # check for duplicates in every row
                if board[i][j] in rowMap[i]:
                    return False
                rowMap[i].add(board[i][j])

                # check for duplicates in every col
                if not j in colMap:
                    colMap[j] = set()
                elif board[i][j] in colMap[j]:
                    return False
                colMap[j].add(board[i][j])
                
                # check for duplicate in every 3 * 3 box
                pointer = math.floor(i / 3) * 3 + math.floor(j / 3)
                if not pointer in boxMap:
                    boxMap[pointer] = set()
                elif board[i][j] in boxMap[pointer]:
                    return False
                boxMap[pointer].add(board[i][j])

        return True