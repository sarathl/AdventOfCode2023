import re
from collections import Counter
import input_reader
input_reader_obj = input_reader.input_reader()

input_clean = input_reader_obj.return_clean_input('inputs/7_input.txt')

hand2bet = {el.split(" ")[0]: int(el.split(" ")[1]) for el in input_clean}

# print(hand2bet)

card_ranking = {'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1}
card_ranking2 = {'A': 13, 'K': 12, 'Q': 11, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1, 'J': 0}

def getCounter(hand):
	h1_counter = {k: v for k, v in sorted(Counter(hand).items(), key=lambda item: item[1], reverse=True)}
	return h1_counter

def getCounter2(hand):
	h1_counter = {k: v for k, v in sorted(Counter(hand).items(), key=lambda item: item[1], reverse=True)}
	if 'J' in h1_counter.keys():
		for k, v in h1_counter.items():
			if k != 'J':
				h1_counter[k] += h1_counter['J']
				break
	h_counter = {k:v for k,v in h1_counter.items() if k!='J'}
	if hand == 'JJJJJ':
		h_counter = {'A': 5}
	return h_counter


def isHand1Better(hand1, hand2, part=1):
	if part == 2:
		h1_counter = getCounter2(hand1)
		h2_counter = getCounter2(hand2)
	else:
		h1_counter = getCounter(hand1)
		h2_counter = getCounter(hand2)
	for (h1_card, h1_card_count), (h2_card, h2_card_count) in zip(h1_counter.items(), h2_counter.items()):
		if h1_card_count > h2_card_count:
			return True
		elif h1_card_count < h2_card_count:
			return False
		else:
			continue
	card_ranking_to_use = card_ranking
	if part == 2:
		card_ranking_to_use = card_ranking2
	for card1, card2 in zip(hand1, hand2):
		if card_ranking_to_use[card1] > card_ranking_to_use[card2]:
			return True
		elif card_ranking_to_use[card1] < card_ranking_to_use[card2]:
			return False
	return False


def bsearch(high, low, ranking_list, curr_hand, part=1):
	mid = (high+low)//2
	mid_hand = ranking_list[mid]
	if high <0:
		ranking_list.insert(0, curr_hand)
		return ranking_list
	elif low > len(ranking_list)-1:
		ranking_list.insert(len(ranking_list), curr_hand)
		return ranking_list
	elif high < low:
		ranking_list.insert(low, curr_hand)
		return ranking_list
	if isHand1Better(mid_hand, curr_hand, part):
		if high == low:
			ranking_list.insert(mid+1, curr_hand)
			return ranking_list
		else:
			low = mid+1
			return bsearch(high, low, ranking_list, curr_hand, part)
	else:
		if high == low:
			ranking_list.insert(mid, curr_hand)
			return ranking_list
		else:
			high = mid-1
			return bsearch(high, low, ranking_list, curr_hand, part)


ranking_list = []
curr_max_rank = 0
for hand in hand2bet.keys():
	if len(ranking_list) == 0:
		ranking_list.append(hand)
	else:
		high = len(ranking_list)-1
		low = 0
		ranking_list = bsearch(high, low, ranking_list, hand)


winnings = 0
max_rank=len(ranking_list)
for idx in range(len(ranking_list)):
	rank = max_rank-idx
	hand=ranking_list[idx]
	bet = hand2bet[hand]
	winnings += (rank*bet)

print(f"Total Winnings are {winnings}")


# Part 2

ranking_list = []
curr_max_rank = 0
for hand in hand2bet.keys():
	if len(ranking_list) == 0:
		ranking_list.append(hand)
	else:
		high = len(ranking_list)-1
		low = 0
		ranking_list = bsearch(high, low, ranking_list, hand, part=2)

print(f"Final Ranking list {ranking_list}")

winnings = 0
max_rank=len(ranking_list)
for idx in range(len(ranking_list)):
	rank = max_rank-idx
	hand=ranking_list[idx]
	bet = hand2bet[hand]
	winnings += (rank*bet)

print(f"Total Winnings are {winnings}")

