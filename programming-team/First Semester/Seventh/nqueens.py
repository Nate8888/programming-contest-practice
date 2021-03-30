def backtrack_n_q(board, col, SIZE): 
	if col >= SIZE: 
		return True

	for i in range(SIZE): 

		if check_surroudings(board, i, col, SIZE): 
			board[i][col] = 1

			if backtrack_n_q(board, col + 1, SIZE) == True: 
				return True

			board[i][col] = 0

	return False

def check_surroudings(board, row, col, SIZE): 

    for i in range(col): 
        if board[row][i] == 1: 
            return False
  
    for i in range(min(row,col)):
        if board[row+(-1*(i+1))][col+(-1*(i+1))] == 1: 
            return False
  
    for i in range(min(SIZE-1-row,col)):
       if board[row+(1*(i+1))][col+(-1*(i+1))] == 1: 
            return False
			
    return True

cases = int(input())
for i in range(cases):
	SIZE = int(input())
	nqueens = [[0] * SIZE for i in range(SIZE)]

	backtrack_n_q(nqueens, 0, SIZE)

	for j in range(SIZE): 
		for i in range(SIZE): 
			if nqueens[i][j] == 1:
				print(i+1, end = " ")
	print()
