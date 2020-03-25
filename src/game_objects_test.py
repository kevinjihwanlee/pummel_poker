import unittest
from game_objects import Card, Deck
from constants import jack, queen, king, ace, spades, hearts, diamonds, clubs, ranks, suits


class TestGameObjectMethods(unittest.TestCase):
	# tests for Card class methods
	def test_card_init(self):
		card = Card(2, spades)
		self.assertEqual(card.suit, spades)
		self.assertEqual(card.rank, 2)
	
	def test_card_compare(self):
		high_card = Card(14, spades)
		low_card = Card(9, hearts)
		same_rank = Card(14, hearts)
		self.assertGreater(high_card, low_card)
		self.assertGreaterEqual(high_card, low_card)
		self.assertLess(low_card, high_card)
		self.assertLessEqual(low_card, high_card)
		self.assertEqual(high_card, same_rank)
		self.assertGreaterEqual(high_card, same_rank)
		self.assertLessEqual(high_card, same_rank)
	
	# tests for Deck class methods
	def test_deck_init(self):
		deck = Deck()
		self.assertEqual(len(deck.cards), 52)

if __name__ == '__main__':
	unittest.main()