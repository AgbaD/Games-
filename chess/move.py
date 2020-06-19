#!/usr/bin/python
# Author:   @BlankGodd
# moving pieces

from main import Board_

class Piece:

	positions = {
			'a1' : (7,1), 'a2' : (6,1), 'a3' : (5,1),
			'a4' : (4,1), 'a5' : (3,1), 'a6' : (2,1),
			'a7' : (1,1), 'a8' : (0,1), 

			'b1' : (7,2), 'b2' : (6,2), 'b3' : (5,2),
			'b4' : (4,2), 'b5' : (3,2), 'b6' : (2,2),
			'b7' : (1,2), 'b8' : (0,2),
			
			'c1' : (7,3), 'c2' : (6,3), 'c3' : (5,3),
			'c4' : (4,3), 'c5' : (3,3), 'c6' : (2,3),
			'c7' : (1,3), 'c8' : (0,3),

			'd1' : (7,4), 'd2' : (6,4), 'd3' : (5,4),
			'd4' : (4,4), 'd5' : (3,4), 'd6' : (2,4),
			'd7' : (1,4), 'd8' : (0,4),

			'e1' : (7,5), 'e2' : (6,5), 'e3' : (5,5),
			'e4' : (4,5), 'e5' : (3,5), 'e6' : (2,5),
			'e7' : (1,5), 'e8' : (0,5),

			'f1' : (7,6), 'f2' : (6,6), 'f3' : (5,6),
			'f4' : (4,6), 'f5' : (3,6), 'f6' : (2,6),
			'f7' : (1,6), 'f8' : (0,6),

			'g1' : (7,7), 'g2' : (6,7), 'g3' : (5,7),
			'g4' : (4,7), 'g5' : (3,7), 'g6' : (2,7),
			'g7' : (1,7), 'g8' : (0,7),

			'h1' : (7,8), 'h2' : (6,8), 'h3' : (5,8),
			'h4' : (4,8), 'h5' : (3,8), 'h6' : (2,8),
			'h7' : (1,8), 'h8' : (0,8)
	}

	alpha = {
			  'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,
			   1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h'
	}	

	def __init__(self,board):
		self.position = Piece._positions
		self.board = board
		self.alpha = Piece._alpha

	def move_pawn_white(self,ab):
		# check if pawn in position a,b-1
		# move to pos a,b
		
		# conditions for move
		cond = False
		ctype  = 0.0
		# ab = b4

		# cond 1
		n = int(ab[-1])
		n -= 1
		m = ab[0]
		ind = self.alpha[m]
		x,y,prev1,prev2 = None,None,None,None
		try:
			x = self.alpha[ind+1]
			y = self.alpha[ind-1]
		except:
			pass
		if x:
			x = self.alpha[x]
			prev1 = x+str(n)
		if y:
			y = self.alpha[y]
			prev2 = y+str(n)

		if prev1:
			prev = self.position[prev1]
			a,b = prev
			if self.board[a][b] == 'p':
				cond = True
				ctype = 1.1
		if not cond:	
			if prev2:
				prev = self.position[prev2]
				a,b = prev
				if self.board[a][b] == 'p':
					cond = True
					ctype = 1.2

		# cond 2
		if not cond:
			n = int(ab[-1])
			n -= 1
			prev_pos = ab[0] + str(n) 
			prev = self.position[prev_pos]
			a,b = prev
			if self.board[a][b] == 'p':
				cond = True
				ctype = 2.0


		# cond 3
		"""if not cond:
			n = int(ab[-1])
			n -= 2
			prev_pos = ab[0] + str(n) 
			prev = self.position[prev_pos]
			a,b = prev
			if self.board[a][b] == 'p':
				cond = True
		"""

		if cond:
			if ctype == 1.1:
				new_pos = self.position[ab]
				prev_pos = self.position[prev1]
				a,b = new_pos
				c,d = prev_pos
				self.board[a][b] = 'p'
				self.board[c][d] = ' '
				print('p{}x{}'.format(prev_pos,new_pos))
			elif ctype == 1.2:
				new_pos = self.position[ab]
				prev_pos = self.position[prev2]
				a,b = new_pos
				c,d = prev_pos
				self.board[a][b] = 'p'
				self.board[c][d] = ' '
				print('p{}x{}'.format(prev_pos,new_pos))
			elif ctype == 2.0:
				new_pos = self.position[ab]
				n = int(ab[-1])
				n -= 1
				prev = ab[0] + str(n) 
				prev_pos = self.position[prev]
				a,b = new_pos
				c,d = prev_pos
				self.board[a][b] = 'p'
				self.board[c][d] = ' '
				print('p{}'.format(new_pos))


