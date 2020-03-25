import unittest
from rule_checker import RuleChecker
from game_objects import Card
from constants import jack, queen, king, ace, spades, hearts, diamonds, clubs, ranks, suits

class TestRuleCheckerMethods(unittest.TestCase):
	def test_flush(self):
		rc = RuleChecker()
		hand_one = [Card(2, spades), Card(5, spades)]
		hand_two = [Card(3, spades), Card(5, diamonds)]
		hand_three = [Card(8, diamonds), Card(10, clubs)]
		board = [Card(4, spades), Card(3, diamonds), Card(6, spades), Card(10, spades)]
		board_with_flush = [Card(4, spades), Card(3, spades), Card(6, spades), Card(10, spades), Card(13, spades)]
		hand_one.extend(board)
		self.assertTrue(rc.is_flush(hand_one))
		hand_two.extend(board)
		self.assertFalse(rc.is_flush(hand_two))
		hand_three.extend(board_with_flush)
		self.assertTrue(rc.is_flush(hand_three))

	def test_straight(self):
		rc = RuleChecker()
		hand_one = [Card(2, spades), Card(6, spades)]
		hand_two = [Card(7, clubs), Card(8, diamonds)]
		hand_three = [Card(14, clubs), Card(2, clubs)]
		hand_four = [Card(14, clubs), Card(10, clubs)]
		hand_five = [Card(14, clubs), Card(2, clubs)]
		hand_six = [Card(14, clubs), Card(2, clubs)]
		board = [Card(4, hearts), Card(3, diamonds), Card(5, spades)]
		board_two = [Card(13, clubs), Card(12, clubs), Card(11, clubs), Card(10, clubs)]
		board_three = [Card(3, clubs), Card(5, clubs), Card(10, diamonds), Card(11, spades), Card(4, hearts)]
		hand_one.extend(board)
		self.assertTrue(rc.is_straight(hand_one))
		hand_two.extend(board)
		self.assertFalse(rc.is_straight(hand_two))
		hand_three.extend(board)
		self.assertTrue(rc.is_straight(hand_three))
		hand_four.extend(board)
		self.assertFalse(rc.is_straight(hand_four))
		hand_five.extend(board_two)
		self.assertTrue(rc.is_straight(hand_five))
		hand_six.extend(board_three)
		self.assertTrue(rc.is_straight(hand_six))
	
	# def test_straight_flush(self):
	# 	rc = RuleChecker()
	# 	hand_one = [Card(2, spades), Card(5, spades)]
	# 	hand_two = [Card(2, spades), Card(14, spades)]
	# 	board = [Card(4, spades), Card(3, spades), Card(6, spades), Card(10, spades)]
	# 	hand_one.extend(board)
	# 	self.assertTrue(rc.is_straight_flush(hand_one))
	# 	hand_two.extend(board)
	# 	self.assertFalse(rc.is_straight_flush(hand_two))



if __name__ == '__main__':
	unittest.main()