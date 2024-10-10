# convert a hand (string) to a list of int representing the value of the cards (0 is strongest the more negative the weaker)
def hand_convert(hand):
    hand_strength = [-strength.index(card) for card in hand]
    return hand_strength

# functions for determining the kind of hand (requires cards to be sorted)
def is_five_kind(hand):
    return hand[0] == hand[4]

def is_four_kind(hand):
    return hand[0] == hand[3] or hand[1] == hand[4]

def is_full_house(hand):
    return (hand[0] == hand[1] and hand[2] == hand[4]) or (hand[0] == hand[2] and hand[3] == hand[4])

def is_three_kind(hand):
    return hand[0] == hand[2] or hand[1] == hand[3] or hand[2] == hand[4]

def is_two_pair(hand):
    check = False
    for i in range(0,4):
        if hand[i] == hand[i+1]:
            if (check):
                return True
            check = True
    return False

def is_one_pair(hand):
    for i in range(0,4):
        if hand[i] == hand[i+1]:
            return True
    return False

# part 1
# parse file
with open("input7.txt") as f:
    lines = f.readlines()
hands = [line.strip().split(" ") for line in lines]

# card possibilities in order from strongest to weakest
strength = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
for hand in hands:
    hand[0] = hand_convert(hand[0])
    hand[1] = int(hand[1])

# assign each hand its kind of hand
for hand in hands:
    if is_five_kind(sorted(hand[0])):
        hand.append(6)
    elif is_four_kind(sorted(hand[0])):
        hand.append(5)
    elif is_full_house(sorted(hand[0])):
        hand.append(4)
    elif is_three_kind(sorted(hand[0])):
        hand.append(3)
    elif is_two_pair(sorted(hand[0])):
        hand.append(2)
    elif is_one_pair(sorted(hand[0])):
        hand.append(1)
    else:
        hand.append(0)

# sort hands from weakest to strongest, first by kind of hand, break ties by value of first card
hands.sort(key=lambda x: (x[2], x[0]))

# sum the value of all hands, weighted by strength
total = 0
for i,hand in enumerate(hands):
    total += hand[1]*(i+1)
print(total)

#part2
# parse file
hands = [line.strip().split(" ") for line in lines]

# card possibilities in order from strongest to weakest (Joker is now weakest)
strength = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
for hand in hands:
    hand[0] = hand_convert(hand[0])
    hand[1] = int(hand[1])

# assign each hand its kind of hand (Jokers aka -12 can improve hands by acting as another card)
for hand in hands:
    if is_five_kind(sorted(hand[0])):
        hand.append(6)
    elif is_four_kind(sorted(hand[0])):
        # either four jokers or one joker to create 5 of a kind
        if -12 in hand[0]:
            hand.append(6)
        else:
            hand.append(5)
    elif is_full_house(sorted(hand[0])):
        # either three jokers or two jokers to create 5 of a kind
        if -12 in hand[0]:
            hand.append(6)
        else:
            hand.append(4)
    elif is_three_kind(sorted(hand[0])):
        # either three jokers or one joker to create 4 of a kind
        if -12 in hand[0]:
            hand.append(5)
        else:
            hand.append(3)
    elif is_two_pair(sorted(hand[0])):
        # two jokers combine with other pair to create 4 of a kind
        if hand[0].count(-12) == 2:
            hand.append(5)
        # one joker combine with a pair to create full house
        elif -12 in hand[0]:
            hand.append(4)
        else:
            hand.append(2)
    elif is_one_pair(sorted(hand[0])):
        # either two jokers or one joker to create 3 of a kind
        if -12 in hand[0]:
            hand.append(3)
        else:
            hand.append(1)
    else:
        # one joker combine with another card to create a pair
        if -12 in hand[0]:
            hand.append(1)
        else:
            hand.append(0)

# sort hands from weakest to strongest, first by kind of hand, break ties by value of first card
hands.sort(key=lambda x: (x[2], x[0]))

# sum the value of all hands, weighted by strength
total = 0
for i,hand in enumerate(hands):
    total += hand[1]*(i+1)
print(total)