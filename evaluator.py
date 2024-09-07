from cards import Card
from deck import Deck
from player import Player
from generateHashTable import HandMap

listOfStraights = [7681, 7936, 3968, 1984, 992, 496, 248, 124, 62, 31]

'''
determines whether a 5-card hand has all unique hands,
which determines if there can be a straight or flush
'''
def isUnique(*cards: Card) -> bool:
    return uniqueBits(*cards) == 5

'''
returns the number of unique cards within a 5-card hand
'''
def uniqueBits(*cards: Card) -> int:
    combinedBits = isUniqueHelper(*cards)
    result = bin(combinedBits).count('1')
    return result

'''
returns the combined 13-bit binary of the 5 poker cards
'''
def isUniqueHelper(*cards: Card) -> int:
    if(len(cards) != 5):
        raise ValueError("Please give a list of 5 cards()")
    result = 0
    for card in cards:
        result |= card.calculateBitForm_()
    return result >> 16

'''
returns whether there is a flush, done by checking the suit bits and using
the bitwise AND operation
'''
def isFlush_cards(*cards: Card) -> bool:
    bitwise_and_result = (cards[0].calculateBitForm_() &
                          cards[1].calculateBitForm_() &
                          cards[2].calculateBitForm_() &
                          cards[3].calculateBitForm_() &
                          cards[4].calculateBitForm_())
    return bool(bitwise_and_result & 0xF000)

def isFlush(*cards: int) -> bool:
    bitwise_and_result = (cards[0] &
                          cards[1] &
                          cards[2] &
                          cards[3] &
                          cards[4])
    return bool(bitwise_and_result & 0xF000)

'''
returns if a hand is a straight using the combined 5-bit
binary value, and returns the "high" of the straight.

if there is no straight, returns -1
    1111000000001 = 5 straight  =   7681
    1111100000000 = 6 straight  =   7936
    0111110000000 = 7 straight  =   3968
    0011111000000 = 8 straight  =   1984
    0001111100000 = 9 straight  =   992
    0000111110000 = 10 straight =   496
    0000011111000 = J straight  =   248
    0000001111100 = Q straight  =   124
    0000000111110 = K straight  =   62
    0000000011111 = A straight  =   31
'''
def isStraight(combinedBits: int) -> int:
    if combinedBits in listOfStraights:
        index = listOfStraights.index(combinedBits)
        return index+5  # Return the index which corresponds to the "high" of the straight
    else:
        return -1

def isStraight_cards(*cards: Card) -> int:
    return isStraight(isUniqueHelper(*cards))
        
'''
Returns the rank of the given hand
'''
def rankHand_cards(*cards: Card) -> int:
    allHands = HandMap()
    primeProduct_ = primeProduct_cards(*cards)
    if isFlush_cards(*cards):
        return allHands.lookUp_table[primeProduct_*2]
    else:
        return allHands.lookUp_table[primeProduct_]

def rankHand(*cards: int) -> int:
    allHands = HandMap()
    primeProduct_ = primeProduct(*cards)
            
    if isFlush(*cards):
        return allHands.lookUp_table[primeProduct_*2]
    else:
        return allHands.lookUp_table[primeProduct_]

'''
Returns the prime product of the cards
'''
def primeProduct_cards(*cards: Card) -> int:
    result = 1
    for card in cards:
        result *= card.calculateBitForm_() & 0xFF
    return result

def primeProduct(*cards: int) -> int:
    result = 1
    for card in cards:
        result *= card & 0xFF
    return result
