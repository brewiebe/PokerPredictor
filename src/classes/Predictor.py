class Predictor:
    def __init__(self, game):
        self.__game = game

    # Returns the probability of getting a hand in between min_wanted and 21
    def probability_win(self, player, min_wanted=19, prob=0):

        # Stop calculating if past 21 or if we have the desired hand
        if min_wanted > 21 or prob >= 1:
            return prob
        else:
            return self.probability_win(player, min_wanted+1, prob+self.probability_hand(player, min_wanted))

    # Returns the probability of busting
    def probability_bust(self, player, prob=0, x=22):
        # Calculate only up to 21+10, Not 21+11 as A is already accounted for in 21-22.
        if x == 32:
            return prob
        else:
            return self.probability_bust(player, prob+self.probability_hand(player, x, True), x+1)

    def probability_hand(self, player, desired_hand, bust=False):
        player_hands = player.total()
        total_probability = 0

        for hand in player_hands:
            probability = 0

            # Hand has busted, return %0
            if hand > 21:
                continue

            # Desired hand achieved, return %100
            if desired_hand <= hand:
                return 1

            card_needed = desired_hand - hand

            # If not calculating bust probability and hand is too low to reach the desired hand, continue to next hand
            if bust is False:
                if card_needed > 11:
                    continue
            else:
                # If calculating bust, A is never counted as 11 only 1
                if card_needed > 10:
                    # Total probability is reset if you cannot bust
                    total_probability = 0
                    continue

            num_cards_known = 0
            for card in self.__game.get_exposed():
                if card.get_int_value() == card_needed or (card_needed == 11 and card.get_int_value() == 1):
                    num_cards_known += 1

            if card_needed == 10:
                probability += (16 - num_cards_known) / (52 - len(self.__game.get_exposed()))
            else:
                probability += (4 - num_cards_known) / (52 - len(self.__game.get_exposed()))

            total_probability += probability

        return total_probability
