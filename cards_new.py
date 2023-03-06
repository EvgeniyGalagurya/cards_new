import itertools
import random
shuf = False


class CardDeck:
    rank = [6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    suit = {'spades' '\u2660', 'hearts' '\u2665',
            'diamonds' '\u2666', 'clubs' '\u2663'}

    def __init__(self):
        self.cards = []
        self.create_deck()

    def create_deck(self):
        self.cards = list(itertools.product(CardDeck.rank, CardDeck.suit))
        return self.cards

    def __str__(self):
        return str(self.cards)

    def shuffle(self):
        global shuf
        shuf = True
        s = self.cards
        s = random.sample(s, len(s))
        return s

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, index):
        if 0 <= index <= (self.__len__()):
            return self.cards[index-1]
        else:
            raise IndexError

    def __add__(self, card):
        self.cards = self.cards + card
        return self.cards

    def __sub__(self, rem_card):
        ind = self.cards.index(rem_card)
        self.cards.pop(ind)
        return self.cards

    def __contains__(self, card):
        return card in self.cards

    def __eq__(self, new_card):
        if isinstance(new_card, CardDeck):
            return self.cards == new_card.cards
        return NotImplemented

    def __bool__(self):
        if shuf is True and bool(self.cards):
            return True
        else:
            return False


class SmallDeck(CardDeck):
    def create_deck(self):
        self.cards = list(itertools.product(CardDeck.rank[1:], CardDeck.suit))
        return self.cards


class ClassicDeck(CardDeck):
    def create_deck(self):
        self.cards = (list(itertools.product([2, 3, 4, 5] +
                      CardDeck.rank, CardDeck.suit)))
        return self.cards


deck1 = CardDeck()
deck2 = CardDeck()
shuffle = False
# deck1.shuffle()
# print(deck1)
# print(deck1.shuffle())
# print(deck1.__len__())
# print(deck1.__getitem__(28))
# print(deck1.__add__([('Q', 'clubs♣')]))
# print(deck1.__len__())
# print(deck1)
# print(deck1.__contains__((6, 'clubs♣')))
# print(deck2)
# print(deck1 == deck2)
# print(deck1.__sub__((7, 'clubs♣')))
# print(type(deck1))
# print(deck1.__len__())
# print(deck1.__bool__())
deck2 = SmallDeck()
print(deck2)
print(deck2.__len__())
# print(deck2.shuffle())
deck3 = ClassicDeck()
print(deck3)
print(deck3.__len__())
