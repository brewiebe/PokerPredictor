class Predictor:
    def __init__(self, game):
        self.__game = game

    def probability_win(self, player, min_wanted=19, prob=0):
        if min_wanted > 21:
            return prob
        y = self.probability_hand(player, min_wanted)
        if y == 0:
            return prob

        return self.probability_win(player, min_wanted+1, prob+y)

    def probability_bust(self, player, prob=0, x=22):
        y = self.probability_hand(player, x, True)
        if y == 0:
            return prob
        else:
            return self.probability_bust(player, prob+y, x+1)

    def probability_hand(self, player, desired_hand, bust=False):
        player_hands = player.total()
        probability = 0

        for hand in player_hands:
            if desired_hand <= hand:
                probability = 1
                break

            card_needed = desired_hand - hand
            if bust is False:
                if card_needed > 11:
                    continue
            else:
                if card_needed >= 11:
                    continue

            num_cards_known = 0
            for card in self.__game.get_exposed():
                if card.get_int_value() == card_needed or (card_needed == 11 and card.get_int_value() == 1):
                    num_cards_known += 1

            if card_needed == 10:
                probability += (16 - num_cards_known) / (52 - len(self.__game.get_exposed()))
            else:
                probability += (4 - num_cards_known) / (52 - len(self.__game.get_exposed()))

        return probability
