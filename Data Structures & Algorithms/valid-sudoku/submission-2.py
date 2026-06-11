class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board[0])

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for i in range(n):
            for j in range(n):
                v = board[i][j]
                if v == '.':
                    continue
                if v in rows[i] or v in cols[j] or v in squares[(i//3)*3+(j//3)]:
                    return False
                rows[i].add(v)
                cols[j].add(v)
                squares[(i//3)*3+(j//3)].add(v)
        return True
