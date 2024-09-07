from __future__ import annotations

rank_map = {
    "2": 0, "3": 1, "4": 2, "5": 3, "6": 4, "7": 5, "8": 6, "9": 7,
    "T": 8, "J": 9, "Q": 10, "K": 11, "A": 12,
}
suit_map = {
    "C": 8, "D": 4, "H": 2, "S": 1,
    "c": 8, "d": 4, "h": 2, "s": 1,
}

primesOfRanks = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41
]


rank_reverse_map = {value: key for key, value in rank_map.items()}
suit_reverse_map = {value: key for key, value in suit_map.items() if key.islower()}

class Card:
    _id: int # _id = rank*4 + suit, 0 < x < 52, deuce of spades to deuce of clubs, then to 3, 4, ..., ace
    _rank: int # int value of the rank
    _suit: int # 1, 2, 4, or 8
    _bitForm: int
    
    def __init__(self, other: int | str | Card) -> None:
        if isinstance(other, int):
            self._id = other
            self._rank = self._id // 4
            self._suit = 2**(3 - (self._id % 4))
            
        if isinstance(other, str):
            if len(other) != 2:
                raise ValueError("The length of the value must be 2! E.g. \"2c\"")
            self._rank = rank_map[other[0]] # still encoded
            self._suit = suit_map[other[1]]
            self._id = self._rank*4 + self._suit
            
        if isinstance(other, Card):
            self._id = other.id_()
            self._rank = other.rank_()
            self._suit = other.suit_()
            
        self._bitForm = self.calculateBitForm_()
    
    def calculateBitForm_(self):
        rank_bits = bin(self._rank)[2:].zfill(4)
        suit_bits = bin(self._suit)[2:].zfill(4)
        prime_index = primesOfRanks[self._rank] if self._rank < len(primesOfRanks) else 0
        prime_bits = bin(prime_index)[2:].zfill(6)  # 6 bits for prime
        # print(f"The rank = {self._rank} and the suit = {self._suit} and the rank_bits = {rank_bits} and the suit_bits = {suit_bits} and the prime = {prime_index:06b}")
        bitmask = [1 if self._rank == i else 0 for i in range(13)]
        bitmask_binary = ''.join(str(bit) for bit in bitmask)
        
        # print(f"The rank = {self._rank} and the suit = {self._suit} and the bitMask = {bitmask_binary}")
        return int(f"000{bitmask_binary}{suit_bits}{rank_bits}00{prime_bits}", 2)
        
    def id_(self) -> int:
        return self._id
    
    def rank_(self) -> int:
        return self._rank
    
    def suit_(self) -> int:
        return self._suit
    
    def printCard_(self):
        print(f"{self._id} " + f"{self._bitForm:032b}")

'''

| rank |    C |    D |    H |    S |
| ---: | ---: | ---: | ---: | ---: |
|    2 |    0 |    1 |    2 |    3 |
|    3 |    4 |    5 |    6 |    7 |
|    4 |    8 |    9 |   10 |   11 |
|    5 |   12 |   13 |   14 |   15 |
|    6 |   16 |   17 |   18 |   19 |
|    7 |   20 |   21 |   22 |   23 |
|    8 |   24 |   25 |   26 |   27 |
|    9 |   28 |   29 |   30 |   31 |
|    T |   32 |   33 |   34 |   35 |
|    J |   36 |   37 |   38 |   39 |
|    Q |   40 |   41 |   42 |   43 |
|    K |   44 |   45 |   46 |   47 |
|    A |   48 |   49 |   50 |   51 |

'''
