#!/usr/bin/python
# Author:	@BlankGodd

import sys

class Tictactoe:
	dic = {1:[0,0],2:[0,1],3:[0,2],4:[1,0],5:[1,1],6:[1,2],7:[2,0],8:[2,1],9:[2,2]}

	def __init__(self):
		# board
		self.bd = [['-','-','-'],['-','-','-'],['-','-','-']]

		print('Welcome to Tictactoe')
		
		print("Help to use board")
		print(' 1 | 2 | 3')
		print('-----------')
		print(' 4 | 5 | 6')
		print('-----------')
		print(' 7 | 8 | 9')

		print("Enter 0 to play against a machine or 1 for two users")
		try:
			c = int(input(": "))
		except:
			print("Invalid input")
			sys.exit(1.5)
		if c == 1:
			self.play()
		else:
			self.play_machine()

	def check_win(self, v):
		if self.bd[0][0] == v and self.bd[0][1] == v and self.bd[0][2] == v:
			return True
		elif self.bd[1][0] == v and self.bd[1][1] == v and self.bd[1][2] == v:
			return True	
		elif self.bd[2][0] == v and self.bd[2][1] == v and self.bd[2][2] == v:
			return True
		elif self.bd[0][0] == v and self.bd[1][0] == v and self.bd[2][0] == v:
			return True
		elif self.bd[0][1] == v and self.bd[1][1] == v and self.bd[2][1] == v:
			return True
		elif self.bd[0][2] == v and self.bd[1][2] == v and self.bd[2][2] == v:
			return True
		elif self.bd[0][0] == v and self.bd[1][1] == v and self.bd[2][2] == v:
			return True
		elif self.bd[0][2] == v and self.bd[1][1] == v and self.bd[2][0] == v:
			return True
		return False

	def set_board(self, player, v):
		pos = 0
		if player == 'p1':
			pos = int(input("Player1: "))
		else:
			pos = int(input("Player2: "))

		if pos == 1:
			self.bd[0][0] == v
		elif pos == 2:
			self.bd[0][1] == v
		elif pos == 3:
			self.bd[0][2] == v
		elif pos == 4:
			self.bd[1][0] == v
		elif pos == 5:
			self.bd[1][1] == v
		elif pos == 6:
			self.bd[1][2] == v
		elif pos == 7:
			self.bd[2][0] == v
		elif pos == 8:
			self.bd[2][1] == v
		elif pos == 9:
			self.bd[2][2] == v
		else:
			print("Invalid position")
			self.set_board(player, v)

	def play(self):
		print("Player 1 to chose X or 0")
		p1 = input(": ").upper()
		if p1 == 'X':
			p2 = 'O'
		elif p1 == 'O':
			p2 = 'X'
		else:
			print("Invalid input")
			self.play()
		self.print_board()
		win_p1 = False
		win_p2 = False
		if win_p1 or win_p2:
			win = True
		else:
			win = False
		count = 1
		while not win:
			print("Enter position to insert tag(X/O)")
			if count%2 == 0:
				self.set_board('p2', p2)
				self.print_board()
				win_p2 = self.check_win(p2)
			else:
				self.set_board('p1', p1)
				self.print_board()
				win_p1 = self.check_win(p1)
			count += 1
			if count == 10:
				break
		if win_p1:
			print('Player1 wins!')
		elif win_p2:
			print('Player2 wins!')
		else:
			print("Draw!")
		cod = input("Enter R to replay or E to exit: ").lower()
		if cod == 'r':
			self.__init__()
		else:
			sys.exit(1)

	def play_machine(self):
		pass
		
	def print_board(self):

		print(' '+self.bd[0][0]+' | '+self.bd[0][1]+' | '+self.bd[0][2])
		print('-----------')
		print(' '+self.bd[1][0]+' | '+self.bd[1][1]+' | '+self.bd[1][2])
		print('-----------')
		print(' '+self.bd[2][0]+' | '+self.bd[2][1]+' | '+self.bd[2][2])

############################################################333

bd = [['-','-','-'],['-','-','-'],['-','-','-']]

def start():

	print('Welcome to Tictactoe')
		
	print("Help to use board")
	print(' 1 | 2 | 3')
	print('-----------')
	print(' 4 | 5 | 6')
	print('-----------')
	print(' 7 | 8 | 9')

	print("Enter 0 to play against a machine or 1 for two users")
	try:
		c = int(input(": "))
	except:
		print("Invalid input")
		sys.exit(1.5)
	if c == 1:
		play()
	else:
		play_machine()


def print_board(bd):

	print(' '+bd[0][0]+' | '+bd[0][1]+' | '+bd[0][2])
	print('-----------')
	print(' '+bd[1][0]+' | '+bd[1][1]+' | '+bd[1][2])
	print('-----------')
	print(' '+bd[2][0]+' | '+bd[2][1]+' | '+bd[2][2])


def check_win(bd,v):
	if bd[0][0] is v and bd[0][1] is v and bd[0][2] is v:
		return True
	elif bd[1][0] is v and bd[1][1] is v and bd[1][2] is v:
		return True	
	elif bd[2][0] is v and bd[2][1] is v and bd[2][2] is v:
		return True
	elif bd[0][0] is v and bd[1][0] is v and bd[2][0] is v:
		return True
	elif bd[0][1] is v and bd[1][1] is v and bd[2][1] is v:
		return True
	elif bd[0][2] is v and bd[1][2] is v and bd[2][2] is v:
		return True
	elif bd[0][0] is v and bd[1][1] is v and bd[2][2] is v:
		return True
	elif bd[0][2] is v and bd[1][1] is v and bd[2][0] is v:
		return True
	return False





print_board(bd)
if check_win(bd, 'O'):
	print(1)
else:
	print(0)