#%%
from typing import List

work_count = { 'A':4, 'K':3, 'Q':2, 'J':1, 'T':.5 }
distribution_count = { 0:3, 1:2, 2:1 }

def suit_quality_adjustments(suit : str) -> float:
    adjustment = 0
    if len(suit) <= 6:
        if 'T' in suit and ('J' in suit or sum(x in suit for x in ['A', 'K', 'Q']) >= 2):
            adjustment += .5
        if '9' in suit and ('T' in suit or '8' in suit or sum(x in suit for x in ['A', 'K', 'Q', 'J']) == 2):
            adjustment += .5
    else:
        adjustment += min(sum(x not in suit for x in ['Q', 'Q', 'J']), min(3, len(suit) - 6))
    return adjustment

def suit_quality(suit : str) -> float:
    return (sum(work_count.get(x, 0) for x in suit) + suit_quality_adjustments(suit)) * len(suit) / 10

def value_ace(suit : str) -> float:
    return 3

def value_king(suit : str) -> float:
    if len(suit) == 1:
        return .5
    return 2

def value_queen(suit : str) -> float:
    if len(suit) == 1:
        return 0
    return .25 + .5 * (len(suit) >= 3) + .25 * ('A' in suit or 'K' in suit)

def value_jack(suit : str) -> float:
    return [0, .25, .5, 0][sum([x in suit for x in ['A', 'K', 'Q']])]

def value_ten(suit : str) -> float:
    higher_honors = sum([x in suit for x in ['A', 'K', 'Q', 'J']])
    if higher_honors == 2:
        return .25
    if (higher_honors ==1) and ('9' in suit):
        return .25
    return 0

value_honors = [('A', value_ace), ('K', value_king), ('Q', value_queen), ('J', value_jack), ('T', value_ten)]

def HCP(suit : str) -> float:
    return sum(f(suit) * (x in suit) for x, f in value_honors )

def distribution_points(hand: List[str]) -> float:
    return max(sum(distribution_count.get(len(suit), 0) for suit in hand) - 1, -.5)

def KnR(hand : List[str]) -> float:
    assert len(hand) == 4
    assert sum(len(suit) for suit in hand) == 13
    return sum(suit_quality(suit.upper()) + HCP(suit.upper()) for suit in hand) + distribution_points(hand)
#%%    
def main():
    hand = input('enter hand:').split()
    while hand:
        print (KnR([x.replace('-','') for x in hand]))
        hand = input('enter hand:').split()
   
#%%
def analyze(hand):
    suits = hand.upper().split()
    for x in suits:
        print (f'{x}: HCP:{HCP(x)}, q:{suit_quality(x)}')
    print (f'dist: {distribution_points(suits)}')
#%%   