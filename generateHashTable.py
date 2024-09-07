from cards import Card
from deck import Deck
import numpy

# from evaluator import *

'''
This file will create a hashmap of all 7462 unique values.
Split into sections of ascending hand strength

Uniques : has 5 cards of unique rank
            e.g. straight, high card (and its flush variants as well)
            
Non-uniques : has 5 cards with non-unique rank
            e.g. one pairs, two pairs, three of a kind, full houses, quads
'''


'''
The max numbers for the different types of hands
'''
MAX_HIGH_CARDS = 1277
MAX_ONE_PAIRS = 4137
MAX_TWO_PAIRS = 4995
MAX_TRIPS = 5853
MAX_STRAIGHTS = 5863
MAX_FLUSHES = 7140
MAX_FULL_HOUSES = 7296
MAX_QUADS = 7452
MAX_STRAIGHT_FLUSHES = 7462

primesOfRanks = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41
]
# straights are identiifed
# use a 13 bit binary to determine:
primesOfStraights = [
    41*2*3*5*7, 2*3*5*7*11, 3*5*7*11*13, 5*7*11*13*17, 7*11*13*17*19,
    11*13*17*19*23, 13*17*19*23*29, 17*19*23*29*31, 19*23*29*31*37, 23*29*31*37*41
]

class HandMap:

    def set(self) -> None:        
        primesMultiplied = 1
        # high card and high card flushes
        rank = 0
        for a in range(0, 9): # rank 12 = Ace, rank 0 = 2
            for b in range(a+1, 10):
                for c in range(b+1, 11):
                    for d in range(c+1, 12):
                        for e in range(d+1, 13):
                            if(len({a, b, c, d, e}) == 5): # if unique
                                primesMultiplied = primesOfRanks[a]*primesOfRanks[b]*primesOfRanks[c]*primesOfRanks[d]*primesOfRanks[e]
                                if primesMultiplied not in primesOfStraights:
                                    self.lookUp_table[primesMultiplied] = rank
                                    self.lookUp_table[primesMultiplied*2] = MAX_STRAIGHTS + rank
                                    # highCard[rank] = primesMultiplied
                                    # print(f"{a+2} {b+2} {c+2} {d+2} {e+2}")
                                    rank += 1

        # print(f"{rank} high cards")
                                
        # one pair
        rank = 0
        primesMultiplied = 1
        
        for pair in range(0, 13):
            for a in range(0, 13):
                for b in range(a+1, 13):
                    for c in range(b+1, 13):
                        if(len({pair, a, b, c}) == 4):
                            primesMultiplied = primesOfRanks[pair]*primesOfRanks[pair]*primesOfRanks[a]*primesOfRanks[b]*primesOfRanks[c]
                            # one_pairs[rank] = primesMultiplied
                            self.lookUp_table[primesMultiplied] = MAX_HIGH_CARDS + rank
                            # print(f"{pair+2} {pair+2} {a+2} {b+2} {c+2}")
                            rank += 1
        
        # print(f"{rank} one pairs")
        
        # two pair - lowest two pair = 2's and 3's + 4
        rank = 0
        for firstPair in range(0, 13):
            for secondPair in range(firstPair+1, 13):
                for a in range(0, 13):
                    if(a != firstPair and a!= secondPair):
                        primesMultiplied = primesOfRanks[firstPair]*primesOfRanks[firstPair]*primesOfRanks[secondPair]*primesOfRanks[secondPair]*primesOfRanks[a]
                        # two_pairs[rank] = primesMultiplied
                        self.lookUp_table[primesMultiplied] = MAX_ONE_PAIRS + rank
                        # print(f"{firstPair+2} {firstPair+2} {secondPair+2} {secondPair+2} {a+2}")
                        rank += 1

        # print(f"{rank} two pairs")

        # trips - lowest trips = 22234
        rank = 0
        for triple in range(0, 13):
            for a in range(0, 13):
                for b in range(a+1, 13):
                    if(len({triple, a, b}) == 3):
                        primesMultiplied = primesOfRanks[triple]*primesOfRanks[triple]*primesOfRanks[triple]*primesOfRanks[a]*primesOfRanks[b]
                        # trips[rank] = primesMultiplied
                        self.lookUp_table[primesMultiplied] = MAX_TWO_PAIRS + rank
                        # print(f"{triple+2} {triple+2} {triple+2} {a+2} {b+2}")
                        rank += 1
        
        # print(f"{rank} trips")
        
        
        # full house
        rank = 0
        for triple in range(0, 13):
            for double in range(0, 13):
                    if(triple != double):
                        primesMultiplied = primesOfRanks[triple]**3 * primesOfRanks[double]**2
                        self.lookUp_table[primesMultiplied] = MAX_FLUSHES + rank
                        # print(f"{triple+2} {triple+2} {triple+2} {double+2} {double+2}")
                        rank += 1

        # print(f"{rank} full houses")
                        
        # quads
        rank = 0
        for quad in range(0, 13):
            for a in range(0, 13):
                    if(quad != a):
                        primesMultiplied = primesOfRanks[quad]**4 * primesOfRanks[a]
                        self.lookUp_table[primesMultiplied] = MAX_FULL_HOUSES + rank
                        # print(f"{quad+2} {quad+2} {quad+2} {quad+2} {a+2}")
                        rank += 1

        # print(f"{rank} quads")
        
        for i in range(0, 10):
            self.lookUp_table[primesOfStraights[i]] = MAX_TRIPS + i
            self.lookUp_table[2 * primesOfStraights[i]] = MAX_QUADS + i
        
    def __init__(self):
        self.lookUp_table = {}
        self.set()
    
    def debugPrint(self):
        for i, (key, value) in enumerate(self.lookUp_table.items()):
            if i >= 7462:
                break
            print(f"{key}: {value}")

    
# handma = HandMap()
# handma.debugPrint()