#!/usr/bin/python
# Author:   @BlankGodd
# main

from board import Board
from move import Move

positions = [
			 'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1',
			 'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2',
			 'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3', 
			 'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4', 
			 'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5', 
			 'a6', 'b6','c6', 'd6', 'e6', 'f6', 'g6', 'h6', 
			 'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7', 
			 'a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'
			 ]
pieces = [
			"p.","p.","p.","p.","p.","p.","p.","p.",
			"R.","N.","B.","K.","Q.","B.","N.","R.",
			"p","p","p","p","p","p","p","p",
			"R","N","B","K","Q","B","N","R"
]

class Start:

	def __init__(self):
		self.bd = Board()
		self.board = self.bd.board
		self.bd.print_board()
		self.move_bot = Move(self.board)
		print('Player1 is white, player2 is black(N.)')
		count = 0
		player = ""
		while True:
			i = 0
			if count == 0 or count % 2 == 0:
				i = 1
			else:
				i = 2
			inp,player = self.get_input(i)
			p,y = self.check_input(inp)
			self.move(p,y,player)
			self.bd.print_board()
			count += 1
			# check win

	def get_input(self,i):
		inp = None
		while not inp:
			print('Player{} '.format(i))
			inp = input(': ')
			if len(inp) == 3:
				break
			else:
				print('Invalid input')
				inp = None
		return inp,i

	def check_input(self,inp):
		p,y = None,None
		
		p = inp[0]
		y = inp[-2] + inp[-1]

		if p in pieces:
			pass
		else:
			print("Invalid move")
			return None

		if y in positions:
			pass
		else:
			print("Invalid move")
			return None
		return p,y

	def move(self,p,y,player):
		if p == 'p':
			self.move_bot.move_pawn(p,y,player)
		if p == 'R' or p == 'R.':
			pass

	

if __name__ == "__main__":
	Start()


