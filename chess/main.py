#!/usr/bin/python
# Author:   @BlankGodd
# main

from board import Board

def start():
	bd = Board()
	bd.print_board()
	inp = get_input()
	
	
def get_input():
	inp = None
	while not inp:
		inp = input('Enter play: ')
		if len(inp) != 3:
			print('Invalid input')
			inp = None
		else:
			break
	return inp


