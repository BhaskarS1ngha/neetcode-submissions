class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hmap = [[False]*9 for _ in range(9)]
        col_hmap = [[False]*9 for _ in range(9)]
        sub_hmap = [[False]*9 for _ in range(9)]

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == '.':
                    continue
                
                val = int(val)-1

                sub_idx = (row//3)*3 + (col//3)

                if row_hmap[row][val] or col_hmap[col][val] or sub_hmap[sub_idx][val]:
                    return False
                
                row_hmap[row][val] = True
                col_hmap[col][val] = True
                sub_hmap[sub_idx][val] = True

        return True