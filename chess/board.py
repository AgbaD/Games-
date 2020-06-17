#!/usr/bin/python
# Author:   @BlankGodd
# chess board

class Board:

	board = [
		[8,"R","N","B","K","Q","B","N","R"], #0
		[7,"p","p","p","p","p","p","p","p"], #1
		[6," "," "," "," "," "," "," "," "], #2
		[5," "," "," "," "," "," "," "," "], #3
		[4," "," "," "," "," "," "," "," "], #4
		[3," "," "," "," "," "," "," "," "], #5
		[2,"p","p","p","p","p","p","p","p"], #6
		[1,"R","N","B","K","Q","B","N","R"], #7
		["","a","b","c","d","e","f","g","h"]
		]

	bd = board

	_positions ={'a1' : bd[7][1], 'a2' : bd[6][1], 'a3' : bd[5][1],
			'a4' : bd[4][1], 'a5' : bd[3][1], 'a6' : bd[2][1],
			'a7' : bd[1][1], 'a8' : bd[0][1], 

			'b1' : bd[7][2], 'b2' : bd[6][2], 'b3' : bd[5][2],
			'b4' : bd[4][2], 'b5' : bd[3][2], 'b6' : bd[2][2],
			'b7' : bd[1][2], 'b8' : bd[0][2],
			
			'c1' : bd[7][3], 'c2' : bd[6][3], 'c3' : bd[5][3],
			'c4' : bd[4][3], 'c5' : bd[3][3], 'c6' : bd[2][3],
			'c7' : bd[1][3], 'c8' : bd[0][3],

			'd1' : bd[7][4], 'd2' : bd[6][4], 'd3' : bd[5][4],
			'd4' : bd[4][4], 'd5' : bd[3][4], 'd6' : bd[2][4],
			'd7' : bd[1][4], 'd8' : bd[0][4],

			'e1' : bd[7][5], 'e2' : bd[6][5], 'e3' : bd[5][5],
			'e4' : bd[4][5], 'e5' : bd[3][5], 'e6' : bd[2][5],
			'e7' : bd[1][5], 'e8' : bd[0][5],

			'f1' : bd[7][6], 'f2' : bd[6][6], 'f3' : bd[5][6],
			'f4' : bd[4][6], 'f5' : bd[3][6], 'f6' : bd[2][6],
			'f7' : bd[1][6], 'f8' : bd[0][6],

			'g1' : bd[7][7], 'g2' : bd[6][7], 'g3' : bd[5][7],
			'g4' : bd[4][7], 'g5' : bd[3][7], 'g6' : bd[2][7],
			'g7' : bd[1][7], 'g8' : bd[0][7],

			'h1' : bd[7][8], 'h2' : bd[6][8], 'h3' : bd[5][8],
			'h4' : bd[4][8], 'h5' : bd[3][8], 'h6' : bd[2][8],
			'h7' : bd[1][8], 'h8' : bd[0][8],
	}
 		

	def print_board(self):
		board = Board.board
		print('\n  ','-'*41)
		for i in range(len(board)-1):
			for j in board[i]:
				print("",j, "|", end=" ")
			print('\n  ','-'*41)
		print('  ',end="")
		for i in board[-1]:
			print(i, end='    ')
		print()




if __name__ == '__main__':
	c = Board()
	c.print_board()