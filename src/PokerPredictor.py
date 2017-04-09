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

for x in range(len(players)):
    print(players[x].to_string())
    print(players[x].total())
    print("Desired Hand:" + str(predictor.probability_win(players[x], 21)*100))
    print("Bust Chance: " + str(predictor.probability_bust(players[x]) * 100))