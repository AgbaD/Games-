#!/usr/bin/python
# Author:   @BlankGodd
# move

from pieces.pawn import Pawn


class Move:

	def __init__(self,board):
		self.board = board

	def move_pawn(self,p,y,player):
		# make the move
		piece = Pawn(self.board)
		piece.move(p,y,player)
		
