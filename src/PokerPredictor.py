from src.classes.Deck import Deck
from src.classes.Player import Player
from src.classes.Game import Game
from src.classes.Predictor import Predictor

deck = Deck()
players = [Player("Daniel", 0.25), Player("Breanne", 0.15), Player("Dealer", 0.10)]

game = Game(players, deck)
predictor = Predictor(game)
game.start_game()

print(players[0].toString())
print(players[0].total())
print(predictor.probability_win(0))
print(players[1].toString())
print(predictor.probability_win(1))
print(players[1].total())
print(players[2].toString())
print(predictor.probability_win(2))
print(players[2].total())
