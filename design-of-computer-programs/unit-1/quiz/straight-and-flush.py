# -----------
# User Instructions
# 
# Define two functions, straight(ranks) and flush(hand).
# Keep in mind that ranks will be ordered from largest
# to smallest.

def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    ranks.sort(reverse=True)
    lastRank = ranks[0]
    ranks = ranks[1:]
    for rank in ranks:
        if ((lastRank - rank) != 1):
            return False
        lastRank = rank
    return True
    # Your code here.

def flush(hand):
    "Return True if all the cards have the same suit."
    suits = [s for r,s in hand]
    lastSuit = suits[0]
    suits = suits[1:]
    for suit in suits:
        if (lastSuit != suit):
            return False
    return True
    # Your code here.
    
def test():
    "Test cases for the functions in poker program."
    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False
    assert flush(sf) == True
    assert flush(fk) == False
    return 'tests pass'

print test()
