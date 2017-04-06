class Card:
    __suit = ""
    __value = ""

    def __init__(self, suit, value):
        self.__suit = suit
        self.__value = value

    def toString(self):
        return self.__value + ":" + self.__suit
