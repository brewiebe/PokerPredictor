class Predictor:
    def __init__(self, game):
        self.__game = game

    def probablility_win(self, player_place):
        player_hand = self.__game.get_players()[player_place].total()
        card_needed = 21 - player_hand
        num_card_needed = 0

        for card in self.__game.get_exposed():
            if card.get_int_value() == card_needed or (card_needed == 11 and card.get_int_value() == 1):
                num_card_needed += 1

        if card_needed == 10:
            probability = (4 - num_card_needed) / (52 - len(self.__game.get_exposed()))
        else:
            probability = (16 - num_card_needed) / (52 - len(self.__game.get_exposed()))

        return probability




