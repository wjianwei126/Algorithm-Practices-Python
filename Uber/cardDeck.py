import random
class Card(object):
    def __init__(self, suit, value):
        if suit not in ['SPADES', 'HEARTS', 'DIAMONDS', 'CLUBS']:
            raise NameError('Suit argument must be SPADES, HEARTS, DIAMONDS or CLUBS!')
        self.suit = suit

        self.valueMap = {'ACE': 1, 'JACK': 11, 'QUEEN': 12, 'KING': 13}
        if isinstance(value, str):
            if value not in ['JACK', 'QUEEN', 'KING']:
                raise NameError('Value argument must be within 1 to 13 or ACE, JACK, QUEEN, KING')
            else:
                self.value = self.valueMap[value]
        else:
            self.value = value

    def getSuitAsString(self):
        return self.suit

    def getValueAsString(self):
        if self.value == 1:
            return 'ACE'
        elif self.value == 11:
            return 'JACK'
        elif self.value == 12:
            return 'QUEEN'
        elif self.value == 13:
            return 'KING'
        else: return str(self.value)

class Deck(object):
    def __init__(self):
        self.suits = ['SPADES', 'HEARTS', 'DIAMONDS', 'CLUBS']
        self.deck = []
        for suit in self.suits:
            for i in range(1, 14):
                self.deck.append(Card(suit, i))

    def shuffle(self):
        #random.shuffle(self.deck)
        shuffledDeck = []
        while self.deck:
            r = random.randint(0, len(self.deck)-1)
            shuffledDeck.append(self.deck[r])
            del self.deck[r]
        self.deck = shuffledDeck

    def printCardsInDeck(self):
        for card in self.deck:
            print card.getSuitAsString() + '-' + card.getValueAsString()


deck = Deck()
# deck.printCardsInDeck()
deck.shuffle()
deck.printCardsInDeck()
