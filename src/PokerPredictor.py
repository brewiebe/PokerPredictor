from src.classes.Deck import Deck
from src.classes.Player import Player

deck = Deck()
exposed = []
players = [Player("Daniel"), Player("Breanne"), Player("Dealer")]

# Deal two cards to each player
for x in range(2):
    for player in players:
        card = deck.draw()

        # Add each dealt card to the known cards, except for the first dealer card as it is face down ass up
        if player.get_name() != "Dealer" or x != 0:
            exposed.append(card)

        player.take(card)

print(players[0].toString())
print(players[1].toString())
print(players[2].toString())


#deck.toString()

