# poker_hand_evaluator

This is a 5-card Poker hand evaluator implementation based on Cactus Kev's algorithm. As this was coded entirely in Python and is to be used for a game, I chose to use classes instead of only integers.

The class HandMap creates a new hash table containing all unique combinations of 5 cards.
The function rankHand() is used to return the rank of the hand, with rankHand(someHand) = 1 being the worst hand, and rankHand(someHand) = 7461 being the best hand, a Royal Flush.
