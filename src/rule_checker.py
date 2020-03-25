import copy, operator
from game_objects import Card
from constants import ace, king

class RuleChecker(object):
	# analyze hand catch all method
	# these should also return a high card

	# TODO documentation
	# this needs to return the hand as well as the relevant high card
	def analyze_hand(self, hand, board):
		both = hand + board
		both.sort()

		is_sf, high = self.is_straight_flush(both)
		if is_sf:
			pass

		is_q, high = self.is_quads(both)
		if is_sf:
			pass

		is_fh, high = self.is_full_house(both)
		if is_fh:
			pass

		is_fl, high = self.is_flush(hand, board)
		if is_fl:
			pass
		
		is_str, high = self.is_straight(both)
		if is_str:
			pass

		is_trip, high = self.is_trips(both)
		if is_trip:
			pass

		is_twop, high = self.is_two_pair(both)
		if is_two_p:
			# TODO ties
			pass

		is_p, high = self.is_pair(both)
		if is_p:
			pass

	def is_flush(self, hand, board):
		both = hand + board
		suit_count = {}
		for card in both:
			curr_suit = card.suit
			suit_count[curr_suit] = suit_count[curr_suit] + 1 if curr_suit in suit_count else 1
		flush_suit = max(suit_count.items(), key=operator.itemgetter(1))[0]
		both.sort(reverse=True)
		high_card = None
		for card in both:
			if card.is_same_suit(flush_suit):
				if card is hand[0]:
					high_card = hand[0]
					break
				elif card is hand[1]:
					high_card = hand[1]
					break
		return (any(count >= 5 for count in suit_count.values()), high_card)

	def is_straight(self, hand):
		end = len(hand)
		min_len = 5
		# edge case for A 2 3 4 5 straight
		if hand[end - 1] == ace:
			# if the first card is not a 2 and the second to last card is not a king
			if hand[0] != 2 and hand[end - 2] != king:
				return False
			end = end - 1
			min_len = 4
		longest = 1
		counter = 1 
		for i in range(1, end):
			if hand[i].rank == hand[i - 1].rank + 1:
				counter = counter + 1
			else:
				# straight ends here and the high card has to be recorded
				counter = 1
			longest = max(longest, counter)
		
		# TODO calculate where exactly the straight ends (look above)

		return longest >= min_len
	
	def is_straight_flush(self, hand):
		# TODO this needs to be adjusted according to the tuple returns
		return self.is_flush(hand) and self.is_straight(hand)

