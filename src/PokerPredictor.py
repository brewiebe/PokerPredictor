from src.classes.Deck import Deck
from src.classes.Player import Player
from src.classes.Game import Game
from src.classes.Predictor import Predictor
from src.classes.Card import Card

deck = Deck()
players = [Player("Dealer", 0.11, True), Player("Daniel", 0.13), Player("Breanne", 0.8), Player("Bob", 0.08), Player("Bert", 0.07), Player("Frank", 0.09)]

game = Game(players, deck)
predictor = Predictor(game)
game.start_game()

for x in range(len(players)):
    print(players[x].to_string())
    print(players[x].total())
    print("Desired Hand:" + str(predictor.probability_hand(players[x], 19) * 100))
    print("Bust Chance: " + str(predictor.probability_bust(players[x]) * 100))
    print("Probability Win: " + str(predictor.probability_win(players[x], 19) * 100) + "\n")

print("Predicted Winning Player(s): ")
for player in predictor.predict_winning_players(players, 19):
    print(player.to_string())

game.play_game(predictor)

print("\n")

print("Winning Player(s): ")
for player in game.get_winner():
    print(player.to_string())
    print(player.total())

print("\nAll Players: ")
for x in range(len(players)):
    print(players[x].to_string())
    print(players[x].total())
