class Player:

    __name = ""
    __hand = []

    def __init__(self, name):
        self.__name = name

    def hit(self, deck):
        self.__hand.append(deck.draw())

    def toString(self):
        txt = self.__name + ": "
        for card in self.__hand:
            txt += "[" + card.toString() + "] "
        return txt
