class Player(object):
	"""A class used to represent a poker player.

	Attributes:
		name: name of the player
		stack: amount of money the player has
		hand: two Cards
	"""

	def __init__(self, name, stack, hand):
		"""Inits Player with name, stack, and two cards that will compose their hand"""
		self.name = name
		self.stack = stack
		self.hand = hand
	
	# TODO fold, bet, receive(?)