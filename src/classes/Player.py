class Player:

    def __init__(self, name):
        self.__name = name
        self.__hand = []

    def get_name(self):
        return self.__name

    def take(self, card):
        self.__hand.append(card)

    def toString(self):
        txt = self.__name + ": "
        for card in self.__hand:
            txt += "[" + card.toString() + "] "
        return txt
