class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board[0])
        seen = {}

        for i in range(n):
            for j in range(n):
                v = board[i][j]
                if v == '.':
                    continue
                if f"r{i}{v}" in seen:
                    return False
                seen[f"r{i}{v}"]=i

                if f"c{j}{v}" in seen:
                    return False
                seen[f"c{j}{v}"]=j

                if f"i{(i//3)*3+(j//3)}{v}" in seen:
                    return False
                seen[f"i{(i//3)*3+(j//3)}{v}"]=(i/3)*3+(j/3)
        return True
