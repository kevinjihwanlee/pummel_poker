import copy
from game_objects import Card
from constants import ace, king

class RuleChecker(object):
	# analyze hand catch all method
	# these should also return a high card

	def analyze_hand(self, hand, board):
		both = hand + board
		# straight flush
		# quads
		# full house
		# flush
		# straight
		# trips
		# two pair
		# pair
		# high card

	def is_flush(self, hand):
		suit_count = {}
		for card in hand:
			curr_suit = card.suit
			suit_count[curr_suit] = suit_count[curr_suit] + 1 if curr_suit in suit_count else 1
		return any(count >= 5 for count in suit_count.values())

	def is_straight(self, hand):
		ordered_hand = copy.deepcopy(hand)
		ordered_hand.sort()
		end = len(ordered_hand)
		min_len = 5
		# edge case for A 2 3 4 5 straight
		if ordered_hand[end - 1] == ace:
			# if the first card is not a 2 and the second to last card is not a king
			if ordered_hand[0] != 2 and ordered_hand[end - 2] != king:
				return False
			end = end - 1
			min_len = 4
		longest = 1
		counter = 1 
		for i in range(1, end):
			if ordered_hand[i].rank == ordered_hand[i - 1].rank + 1:
				counter = counter + 1
			else:
				counter = 1
			longest = max(longest, counter)
		return longest >= min_len
	
	def is_straight_flush(self, hand):
		return self.is_flush(hand) and self.is_straight(hand)

