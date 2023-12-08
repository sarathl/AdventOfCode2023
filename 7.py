import re
from collections import Counter
import input_reader
input_reader_obj = input_reader.input_reader()

input_clean = input_reader_obj.return_clean_input('inputs/7_input.txt')

hand2bet = {el.split(" ")[0]: int(el.split(" ")[1]) for el in input_clean}


card_ranking = {'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 3, '2': 1}

def isHand1Better(hand1, hand2):
	h1_counter = {k: v for k, v in sorted(Counter(hand1).items(), key=lambda item: item[1], reverse=True)}
	h2_counter = {k: v for k, v in sorted(Counter(hand2).items(), key=lambda item: item[1], reverse=True)}
	for (h1_card, h1_card_count), (h2_card, h2_card_count) in zip(h1_counter.items(), h2_counter.items()):
		if h1_card_count > h2_card_count:
			return True
		elif h1_card_count < h2_card_count:
			return False
		else:
			if card_ranking[h1_card] > card_ranking[h2_card]:
				return True
			elif card_ranking[h1_card] < card_ranking[h2_card]:
				return False
	return False


def bsearch(high, low, ranking_list, curr_hand):
	mid = (high+low)//2
	mid_hand = ranking_list[mid]
	if curr_hand == 'AA5AA':
		print(f"Comparing - {mid} - {mid_hand}")
	if isHand1Better(mid_hand, curr_hand):
		if mid == len(ranking_list)-1:
			ranking_list.insert(mid+1, curr_hand)
			return ranking_list
		elif mid == len(ranking_list)-2:
			if isHand1Better(ranking_list[-1], curr_hand):
				ranking_list.insert(len(ranking_list), curr_hand)
			else:
				ranking_list.insert(len(ranking_list)-1, curr_hand)
			return ranking_list
		elif isHand1Better(curr_hand, ranking_list[mid+1]):
			ranking_list.insert(mid+1, curr_hand)
			return ranking_list
		else:
			low = mid+1
			return bsearch(high, low, ranking_list, curr_hand)
	else:
		if mid - 1 < 0:
			if isHand1Better(curr_hand, ranking_list[0]):
				ranking_list.insert(0, curr_hand)
			else:
				ranking_list.insert(1, curr_hand)
			return ranking_list
		elif mid == 1:
			if isHand1Better(curr_hand, ranking_list[1]):
				if isHand1Better(curr_hand, ranking_list[0]):
					ranking_list.insert(0, curr_hand)
				else:
					ranking_list.insert(1, curr_hand)
			else:
				ranking_list.insert(2, curr_hand)
			return ranking_list
		elif isHand1Better(ranking_list[mid-1], curr_hand):
			ranking_list.insert(mid-1, curr_hand)
			return ranking_list
		else:
			high = mid-1
			return bsearch(high, low, ranking_list, curr_hand)




ranking_list = []
curr_max_rank = 0
for hand in hand2bet.keys():
	if len(ranking_list) == 0:
		ranking_list.append(hand)
	else:
		high = len(ranking_list)-1
		low = 0
		if hand == 'AA5AA':
			print(ranking_list)
		ranking_list = bsearch(high, low, ranking_list, hand)


print(f"Final Ranking List is {ranking_list}")

winnings = 0
max_rank=len(ranking_list)
for idx in range(len(ranking_list)):
	rank = max_rank-idx
	hand=ranking_list[idx]
	bet = hand2bet[hand]
	# print(f"Hand is {hand}, rank is {rank}, bet is {bet}")
	winnings += rank*bet

print(f"Total Winnings are {winnings}")
