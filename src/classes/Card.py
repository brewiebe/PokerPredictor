class Card:

    def __init__(self, suit, value, int_value):
        self.__suit = suit
        self.__value = value
        self.__int_value = int_value

    def get_value(self):
        return self.__value

    def toString(self):
        return self.__value + ":" + self.__suit

    def get_int_value(self):
        return self.__int_value