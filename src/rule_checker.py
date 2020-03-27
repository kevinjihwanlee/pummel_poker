import copy, operator
from game_objects import Card
from constants import ace, king, straight_flush, quads, full_house, flush, straight, trips, two_pair, pair, high_card

class RuleChecker(object):
	def analyze_hand(self, hand, board):
		"""Returns hand classification, rank (rank, [rank], None), relevant high card (either Card or [Card]) """
		is_sf, high_card = self.is_straight_flush(hand, board)
		if is_sf:
			return(straight_flush, None, high_card)

		is_q, rank, high_card = self.is_quads(hand, board)
		if is_q:
			return(quads, rank, high_card)

		is_fh, trips_rank, pair_rank = self.is_full_house(hand, board)
		if is_fh:
			return(full_house, [trips_rank, pair_rank], None)

		is_fl, high_card = self.is_flush(hand, board)
		if is_fl:
			return(flush, None, high_card)
		
		is_str, high_card = self.is_straight(hand, board)
		if is_str:
			return(straight, None, high_card)

		is_trip, rank, high_card = self.is_trips(hand, board)
		if is_trip:
			return(trips, rank, high_card)

		is_twop, higher_rank, lower_rank, high_card = self.is_two_pair(hand, board)
		if is_twop:
			return(two_pair, [higher_rank, lower_rank], high_card)

		is_p, rank, high_card = self.is_pair(hand, board)
		if is_p:
			return(pair, rank, high_card)
		
		# Top five cards of the hand + board
		both = hand + board
		both.sort(reverse=True)
		high_cards = list(map(lambda card: card.rank, both[0:5]))
		return(high_card, None, high_cards)

	def is_straight_flush(self, hand, board):
		# Flush high card trumps straight high card 
		is_s, high_card = self.is_straight(hand, board)
		is_f, high_card = self.is_flush(hand, board)
		return (is_f and is_s, high_card)
	
	def is_quads(self, hand, board):
		# Fifth card (highest outside the quads) in the hand + board is the kicker
		both = hand + board
		count = {}
		for card in both:
			rank = card.rank
			count[rank] = count[rank] + 1 if rank in count else 1
		rank, rank_count = max(count.items(), key=operator.itemgetter(1))
		if rank_count == 4:
			both.sort(reverse=True)
			for card in both:
				if card != rank:
					high_card = card
					break
			return (True, rank, high_card)
		else:
			return (False, None, None)

	def is_full_house(self, hand, board):
		has_pair, pair_rank, pair_high_cards = self.is_pair(hand, board)
		has_trips, trips_rank, trips_high_cards = self.is_trips(hand, board)
		if has_pair and has_trips and pair_rank != trips_rank:
			return (True, trips_rank, pair_rank)
		else:
			return (False, None, None)

	def is_flush(self, hand, board):
		# If flush is completed with hand, high card is within hand, otherwise no high card
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

	def is_straight(self, hand, board):
		# High card is determined by the straight either on board or completed by hand
		both = hand + board
		both.sort()
		min_len = 5
		end = len(both)
		# edge case for aces
		if both[end - 1] == ace:
			# create duplicate ace at the beginning
			both.insert(0, Card(1, both[end - 1].suit))
			end = len(both)
		longest = 1
		counter = 1
		high_card = None
		for i in range(1, end):
			if both[i].rank == both[i - 1].rank + 1:
				if counter >= min_len:
					high_card = both[i]
				counter = counter + 1
			else:
				if counter >= min_len:
					high_card = both[i - 1]
				counter = 1
			longest = max(longest, counter)
		if longest >= min_len and longest == counter:
			high_card = both[end - 1]
		return (longest >= min_len, high_card)
	
	def is_trips(self, hand, board):
		# Fourth and fifth card (highest outside trips) in the hand + board is the kicker
		both = hand + board
		count = {}
		for card in both:
			rank = card.rank
			count[rank] = count[rank] + 1 if rank in count else 1
		rank, rank_count = max(count.items(), key=operator.itemgetter(1))
		if rank_count == 3:
			high_cards = []
			both.sort(reverse=True)
			for card in both:
				if card != rank:
					high_cards.append(card)
					if len(high_cards) == 2:
						break
			return (True, rank, high_cards)
		else:
			return (False, None, None)
		
	def is_two_pair(self, hand, board):
		# Highest pair is the winner, in case of tie the fifth card kicker is the winner
		# TODO DRY abstract this out to a generic pair_finder fn
		both = hand + board
		count = {}
		for card in both:
			rank = card.rank
			count[rank] = count[rank] + 1 if rank in count else 1
		sorted_counts = sorted(count.items(), key=operator.itemgetter(1), reverse=True)
		pairs = filter(lambda x: x[1] == 2, sorted_counts)
		pairs = list(map(lambda x: x[0], pairs))
		if len(pairs) >= 2:
			# TODO ugly...clean it up at some point
			higher_rank = pairs[0] if pairs[0] > pairs[1] else pairs[1]
			lower_rank = pairs[1] if pairs[0] > pairs[1] else pairs[0]
			both.sort(reverse=True)
			for card in both:
				if card != pairs[0] and card != pairs[1]:
					high_card = card
					break
			return (True, higher_rank, lower_rank, high_card)
		else:
			return (False, None, None, None)
	
	def is_pair(self, hand, board):
		# TODO DRY abstract this out to a generic pair_finder fn
		both = hand + board
		count = {}
		for card in both:
			rank = card.rank
			count[rank] = count[rank] + 1 if rank in count else 1
		sorted_counts = sorted(count.items(), key=operator.itemgetter(1), reverse=True)
		pairs = filter(lambda x: x[1] == 2, sorted_counts)
		pairs = list(map(lambda x: x[0], pairs))
		if len(pairs) >= 1:
			rank = pairs[0]
			high_cards = []
			both.sort(reverse=True)
			for card in both:
				if card != rank:
					high_cards.append(card)
					if len(high_cards) == 3:
						break
			return (True, rank, high_cards)
		else:
			return (False, None, None)

