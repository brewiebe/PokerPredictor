from src.classes.Deck import Deck
from src.classes.Player import Player
from src.classes.Game import Game
from src.classes.Predictor import Predictor

correctly_predicted = 0
incorrectly_predicted = 0

for x in range(10):
    print("\n\n--------------Game #" + str(x) + "-----------------")

    deck = Deck()
    players = [Player("Dealer", 0.50, True), Player("Daniel", 0.56), Player("Breanne", 0.8), Player("Bob", 0.75), Player("Bert", 0.60), Player("Frank", 0.60)]

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
    pred_winning_player = predictor.predict_winning_players(players, 19)
    for player in pred_winning_player:
        print(player.to_string())

    game.play_game(predictor)

    print("\n")

    print("Winning Player(s): ")
    winning_player = game.get_winner()
    for player in winning_player:
        print(player.to_string())
        print(player.total())

    print("\nAll Players: ")
    for x in range(len(players)):
        print(players[x].to_string())
        print(players[x].total())

    correct_pred = list(set(pred_winning_player).intersection(winning_player))
    if len(correct_pred) > 0:
        correctly_predicted += 1
    else:
        incorrectly_predicted += 1

print("\nCorrectly Predicted Games: " + str(correctly_predicted / 10 * 100) + "%")




