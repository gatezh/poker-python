# You may assume the following behavior of each function:
#
# straight(ranks): returns True if the hand is a straight.
# flush(hand):     returns True if the hand is a flush.
# kind(n, ranks):  returns the first rank that the hand has
#                  exactly n of. For A hand with 4 sevens
#                  this function would return 7.
# two_pair(ranks): if there is a two pair, this function
#                  returns their corresponding ranks as a
#                  tuple. For example, a hand with 2 twos
#                  and 2 fours would cause this function
#                  to return (4, 2).
# card_ranks(hand) returns an ORDERED tuple of the ranks
#                  in a hand (where the order goes from
#                  highest to lowest rank).

def poker(hands):
    "Return the best hand: poker([hand,...] => hand)"
    return max(hands, key=hand_rank)

def hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):                              # flush
        return (5, [ranks])
    elif straight(ranks):                          # straight
        return (4, max(ranks))
    elif kind(3, ranks):                           # 3 of a kind
        return (3, max(ranks), ranks)
    elif two_pair(ranks):                          # 2 pair
        return (2, kind(3, ranks), kind(2, ranks), ranks)
    elif kind(2, ranks):                           # kind
        return (1, ranks)
    else:                                          # high card
        return (0, ranks)

def card_ranks(cards):
    "Return a list of the ranks, sorted with higher first."
    ranks = ["--23456789TJQKA".index(r) for r,s in cards]
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks
    
def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    count = 0
    for i in range(0, 4):
        if (ranks[i] - 1) == ranks[i + 1]:
            count += 1
    if count == 4:
        return True
    else:
        return False

def flush(hand):
    "Return True if all the cards have the same suit."
    suits = [s for r,s in hand]
    count = 0
    for i in range(0, 4):
        if suits[i] == suits[i + 1]:
            count += 1
    if count == 4:
        return True
    else:
        return False

def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    for i in ranks:
        if n == ranks.count(i):
            return i
    return None

def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    highest = None
    lowest = None
    for i in ranks:
        if ranks.count(i) == 2:
            highest = i
            break
    for i in ranks[::-1]:
        if ranks.count(i) == 2:
            if highest != i:
                lowest = i
                break
    if (highest == None) or (lowest == None):
        return None
    return (highest, lowest)

def test():
    "Test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]
    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([sf]) == sf
    assert poker([sf] + 99*[fh]) == sf
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
    return 'tests pass'

print test()
