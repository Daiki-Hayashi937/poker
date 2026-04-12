import random

SUITS = ['D', 'H', 'S', 'C']
VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


class Deck:
    def __init__(self):
        self.cards = [s + v for s in SUITS for v in VALUES]
        random.shuffle(self.cards)

    def deal(self, n):
        cards = [self.cards.pop(0) for _ in range(n)]
        cards.sort()
        return cards

    def redraw(self, hand, indices):
        new_cards = self.deal(len(indices))
        for i, idx in enumerate(indices):
            self.cards.append(hand[idx])
            hand[idx] = new_cards[i]
        hand.sort()
        return hand
