#!/usr/bin/python
# Author:   @BlankGodd
# chess

class Chess:

	def __init__(self):
		self.board = [
		["R","N","B","K","Q","B","N","R"],
		["p","p","p","p","p","p","p","p"],
		["","","","","","","",""],
		["","","","","","","",""],
		["","","","","","","",""],
		["","","","","","","",""],
		["p","p","p","p","p","p","p","p"],
		["R","N","B","K","Q","B","N","R"]
		]

	def draw_board(self):
