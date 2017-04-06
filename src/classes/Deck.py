from random import randint
from .Card import Card


class Deck:
    __cards = []

    def __init__(self):
        suits = ("Heart", "Spade", "Diamond", "Club")
        values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

        for suit in suits:
            for value in values:
                self.__cards.append(Card(suit, value))

    def get_count(self):
        return len(self.__cards)

    def draw(self):
        return self.__cards.pop(randint(0, self.get_count()))

    def toString(self):
        for card in self.__cards:
            print(card.toString())
