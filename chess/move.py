#!/usr/bin/python
# Author:   @BlankGodd
# move

from pieces.pawn import Pawn
from pieces.rook import Rook
from pieces.positions import Pos


class Move:

	def __init__(self,board):
		self.position = Pos._positions
		self.board = board
		self.alpha = Pos._alpha

	def move_pawn(self,p,y,player):
		# make the move
		piece = Pawn(self.board)
		move = piece.move(p,y,player)
		if move:
			num = y[-1]
			if num == 8 and player == 1:
				while True:
					print('Change piece to...')
					print('1.Rook')
					print('2.Knight')
					print('3.Bishop')
					print('4.Queen')
					ch = int(input(': '))
					a,b = self.position[y]
					if ch == 1:
						self.board[a][b] = 'R '
						break
					elif ch == 2:
						self.board[a][b] = 'N '
						break
					elif ch == 3:
						self.board[a][b] = 'B '
						break
					elif ch == 4:
						self.board[a][b] = 'Q '
						break
					else:
						print('Invalid input')
			elif num == 1 and player == 2:
				while True:
					print('Change piece to...')
					print('1.Rook')
					print('2.Knight')
					print('3.Bishop')
					print('4.Queen')
					ch = int(input(': '))
					a,b = self.position[y]
					if ch == 1:
						self.board[a][b] = 'R.'
						break
					elif ch == 2:
						self.board[a][b] = 'N.'
						break
					elif ch == 3:
						self.board[a][b] = 'B.'
						break
					elif ch == 4:
						self.board[a][b] = 'Q.'
						break
					else:
						print('Invalid input')

		return move

	def move_rook(self,p,y,player):
		piece = Rook(self.board)
		move = piece.move(p,y,player)
		if not move:
			print('Invalid move')
		return move


