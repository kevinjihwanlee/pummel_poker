import unittest
from rule_checker import RuleChecker
from game_objects import Card
from constants import jack, queen, king, ace, spades, hearts, diamonds, clubs, ranks, suits

class TestRuleCheckerMethods(unittest.TestCase):
	def test_straight_flush(self):
		rc = RuleChecker()
		hand_one = [Card(2, spades), Card(5, spades)]
		hand_two = [Card(2, spades), Card(14, spades)]
		board = [Card(4, spades), Card(3, spades), Card(6, spades), Card(10, spades)]
		self.assertTrue(rc.is_straight_flush(hand_one, board)[0])
		self.assertFalse(rc.is_straight_flush(hand_two, board)[0])
	
	def test_quads(self):
		rc = RuleChecker()
		hand_one = [Card(2, spades), Card(6, spades)]
		hand_two = [Card(2, spades), Card(3, spades)]
		board = [Card(2, diamonds), Card(2, hearts), Card(2, clubs), Card(5, diamonds)]
		self.assertTrue(rc.is_quads(hand_one, board)[0])
		self.assertEqual(rc.is_quads(hand_one, board)[1], 2)
		self.assertEqual(rc.is_quads(hand_one, board)[2], 6)
		self.assertEqual(rc.is_quads(hand_two, board)[2], 5)

	def test_flush(self):
		rc = RuleChecker()
		hand_one = [Card(2, clubs), Card(5, clubs)]
		hand_two = [Card(3, spades), Card(4, diamonds)]
		hand_three = [Card(8, diamonds), Card(10, clubs)]
		board = [Card(4, clubs), Card(6, clubs), Card(10, clubs), Card(5, spades)]
		board_with_flush = [Card(4, spades), Card(3, spades), Card(6, spades), Card(10, spades), Card(13, spades)]
		self.assertTrue(rc.is_flush(hand_one, board)[0])
		self.assertFalse(rc.is_flush(hand_two, board)[0])
		self.assertTrue(rc.is_flush(hand_three, board_with_flush)[0])

	def test_straight(self):
		rc = RuleChecker()
		hand_one = [Card(2, spades), Card(6, spades)]
		hand_two = [Card(7, clubs), Card(8, diamonds)]
		hand_three = [Card(2, spades), Card(13, hearts)]
		board = [Card(4, hearts), Card(3, diamonds), Card(5, spades)] 
		board_two = [Card(4, hearts), Card(3, diamonds), Card(5, spades), Card(6, hearts)]
		self.assertTrue(rc.is_straight(hand_one, board)[0])
		self.assertEqual(rc.is_straight(hand_one, board)[1], 6)
		self.assertFalse(rc.is_straight(hand_two, board)[0])
		self.assertTrue(rc.is_straight(hand_one, board_two)[0])
		self.assertTrue(rc.is_straight(hand_two, board_two)[0])
		self.assertTrue(rc.is_straight(hand_three, board_two)[0])

		# Ace straight edge cases
		hand_one = [Card(14, spades), Card(2, hearts)]
		board = [Card(4, hearts), Card(3, diamonds), Card(5, spades)] 
		board_two = [Card(13, hearts), Card(12, diamonds), Card(11, spades), Card(10, spades)] 
		self.assertTrue(rc.is_straight(hand_one, board)[0])
		self.assertEqual(rc.is_straight(hand_one, board)[1], 5)
		self.assertTrue(rc.is_straight(hand_one, board_two)[0])
		self.assertEqual(rc.is_straight(hand_one, board_two)[1], 14)

		# Straight on board 
		hand_one = [Card(14, spades), Card(14, hearts)]
		hand_two = [Card(14, diamonds), Card(8, diamonds)]
		board_with_straight = [Card(4, hearts), Card(3, diamonds), Card(5, spades), Card(6, hearts), Card(7, clubs)]
		self.assertTrue(rc.is_straight(hand_one, board_with_straight)[0])
		self.assertEqual(rc.is_straight(hand_one, board_with_straight)[1], 7)
		self.assertEqual(rc.is_straight(hand_two, board_with_straight)[1], 8)




if __name__ == '__main__':
	unittest.main()