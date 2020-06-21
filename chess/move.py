#!/usr/bin/python
# Author:   @BlankGodd
# move

from pieces.pawn import Pawn
from pieces.rook import Rook


class Move:

	def __init__(self,board):
		self.board = board

	def move_pawn(self,p,y,player):
		# make the move
		piece = Pawn(self.board)
		move = piece.move(p,y,player)
		return move

	def move_rook(self,p,y,player):
		piece = Rook(self.board)
		move = piece.move(p,y,player)
		if not move:
			print('Invalid move')
		return move


