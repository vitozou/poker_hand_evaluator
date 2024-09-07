from cards import Card
from random import shuffle

NUM_RANKS = 13

class Deck:
    
    
    def __init__(self):
        self._deck = []
        self.fillDeck()
        self.shuffleDeck()
    
    def fillDeck(self):
        for rank in range(NUM_RANKS):
            for suit in range(4):
                cardID = 4*(rank) + suit
                newCard = Card(cardID)
                self._deck.append(newCard)
    
    def shuffleDeck(self) -> None:        
        shuffle(self._deck)

    def printDeck(self):
        for card in self._deck:
            card.printCard_()
        print(f"{len(self._deck)}")
            
    def dealCard(self) -> int:
        return self._deck.pop(0)
    
    def getDeck(self):
        return self._deck
    
    def setDeck(self, newDeck):
        _deck = newDeck
            
deck = Deck()
# deck.shuffleDeck()
# deck.shuffleDeck()
# deck.printDeck()