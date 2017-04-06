class Card:

    def __init__(self, suit, value):
        self.__suit = suit
        self.__value = value

    def get_value(self):
        return self.__value

    def toString(self):
        return self.__value + ":" + self.__suit