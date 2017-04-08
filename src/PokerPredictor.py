from src.classes.Deck import Deck
from src.classes.Player import Player
from src.classes.Game import Game
from src.classes.Predictor import Predictor
from src.classes.Card import Card

deck = Deck()
players = [Player("Daniel", 0.25), Player("Breanne", 0.15), Player("Bob", 0.10), Player("Bert", 0.25), Player("Frank", 0.15), Player("Dealer", 0.10)]

game = Game(players, deck)
predictor = Predictor(game)
game.start_game()

print(players[0].to_string())
print(players[0].total())
print(predictor.probability_win(0))
print(players[1].to_string())
print(predictor.probability_win(1))
print(players[1].total())
print(players[2].to_string())
print(predictor.probability_win(2))
print(players[2].total())
print(players[3].to_string())
print(predictor.probability_win(3))
print(players[3].total())
print(players[4].to_string())
print(predictor.probability_win(4))
print(players[4].total())
print(players[5].to_string())
print(predictor.probability_win(5))
print(players[5].total())
