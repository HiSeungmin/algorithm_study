# 2580 : 스도쿠

def dfs(i, j):
    pass

sudoku = [ list(map(int, input().split())) for _ in range(9)]

for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0 :
                dfs(i,j) 
