
import random
from constants import ranks, suits

class Deck(object):
	"""A class used to represent a playing deck.

	Attributes:
		cards: List of Cards (52 in total, 13 of each suit)
	"""

	def __init__(self):
		temp_cards = []
		for rank in ranks:
			for suit in suits:
				card = Card(rank, suit)
				temp_cards.append(card)
		self.cards = temp_cards
	
	def shuffle(self):
		random.shuffle(self.cards)


class Card(object):
	"""A class used to represent a playing card.

	Attributes:
		rank: Rank of the card (2 - 10, Jack, Queen, King, or Ace)
		suit: Suit of the card (spades, clubs, hearts, diamonds)
	"""

	def __init__(self, rank, suit):
		"""Inits Card given rank and suit"""
		self.rank = rank
		self.suit = suit
	
	def __repr__(self):
		# TODO more human readable in future?
		return f"{self.rank} of {self.suit}"

	def __eq__(self, obj):
		return ((isinstance(obj, Card) and self.rank == obj.rank) or
						(isinstance(obj, int) and self.rank == obj))

	def __ne__(self, obj):
		return not self == obj
	
	def __lt__(self, obj):
		return ((isinstance(obj, Card) and self.rank < obj.rank) or
						(isinstance(obj, int) and self.rank < obj))
	
	def __le__(self, obj):
		return self == obj or self < obj

	def __gt__(self, obj):
		return ((isinstance(obj, Card) and self.rank > obj.rank) or
						(isinstance(obj, int) and self.rank > obj))
	
	def __ge__(self, obj):
		return self == obj or self > obj
	
	def is_same_suit(self, suit):
		# TODO enforce contract of suit options?
		return self.suit == suit

	