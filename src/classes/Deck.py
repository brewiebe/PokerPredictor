from random import randint
from .Card import Card


class Deck:

    def __init__(self):
        suits = ("Heart", "Spade", "Diamond", "Club")
        values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
        int_values = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)
        self.__cards = []

        for suit in suits:
            for x in range(len(values)):
                self.__cards.append(Card(suit, values[x], int_values[x]))

    def get_count(self):
        return len(self.__cards)

    def draw(self):
        return self.__cards.pop(randint(0, self.get_count()-1))

    def toString(self):
        for card in self.__cards:
            print(card.toString())
