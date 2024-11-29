import random

class card_deck:
    def __init__(self, rank, suite, card):
        self.rank= rank
        self.suite = suite
    def ranks(self):
        return self.rank
    def suites(self):
        return self.suite
    def cards(self,card):
        suit_name= ['The suit of Spades','The suit of Hearts', 'The suit of Diamonds','Clubs']
        rank_name=['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']


    def value(self):
        if self.rank == 'Ace':
            return 1
        elif self.rank == 'Jack':
            return 11
        elif self.rank == 'Queen':
            return 12
        elif self.rank == 'King':
          return 13
    def shffule(self):
        random.shuffle(self.cards)
    def remove(self,card):
        self.cards.remove(card)


    def cardremaining(self):
        self.suite-self.rank

    def main(self):
        try:
            deck=[]
            for i in ['Spades','Hearts', ' Diamonds','Clubs']:
                for c in ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']:
                    deck.append((c, i))
            deck.shff

            hand = []
            user =eval(input('Enter a number of cards: 1-7 '))
            print()
            while user <1 or user >7:
                print ("Only a number between 1-7:")
                return

            for i in range(user):
                hand.append(deck[i])
            print (hand)
        except ValueError:
            print("Only numbers")
    main()