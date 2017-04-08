class Predictor:
    def __init__(self, game):
        self.__game = game

    def probability_win(self, player_place):
        player = self.__game.get_players()[player_place]
        prob_19 = self.probability_hand(player, 19)
        prob_20 = self.probability_hand(player, 20)
        prob_21 = self.probability_hand(player, 21)
        prob_over_21 = self.probability_bust(player)
        return (prob_19 + prob_20 + prob_21) - prob_over_21

    def probability_hand(self, player, desired_hand):
        player_hands = player.total()
        probability = 0

        for hand in player_hands:
            if desired_hand < hand:
                break
            card_needed = desired_hand - hand
            if card_needed > 11:
                break
            num_card_needed = 0
            for card in self.__game.get_exposed():
                if card.get_int_value() == card_needed or (card_needed == 11 and card.get_int_value() == 1):
                    num_card_needed += 1

            if card_needed == 10:
                probability += (4 - num_card_needed) / (52 - len(self.__game.get_exposed()))
            else:
                probability += (16 - num_card_needed) / (52 - len(self.__game.get_exposed()))

        return probability

    def probability_bust(self, player):
        player_hands = player.total()
        probability = 0

        for hand in player_hands:
            # calculate card needed for getting 21
            card_needed = 21 - hand

            if card_needed > 11 or card_needed <= 0:
                break
            # anything higher than the card needed will cause a bust
            for card in range(card_needed + 1, 11):
                num_card_needed = 0
                for ex_card in self.__game.get_exposed():
                    if ex_card.get_int_value() == card or (card == 11 and ex_card.get_int_value() == 1):
                        num_card_needed += 1

                if card == 10:
                    probability += (4 - num_card_needed) / (52 - len(self.__game.get_exposed()))
                else:
                    probability += (16 - num_card_needed) / (52 - len(self.__game.get_exposed()))

        return probability
