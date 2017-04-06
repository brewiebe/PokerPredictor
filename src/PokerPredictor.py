from src.classes.Deck import Deck
from src.classes.Player import Player

deck = Deck()
p1 = Player("Daniel")

p1.hit(deck)
p1.hit(deck)
print(deck.get_count())

print(p1.toString())

deck.toString()

