class Player:

    def __init__(self, name, risk):
        self.__name = name
        # cards player is holding
        self.__hand = []
        # probablility of getting blackjack needed for player to draw
        self.__risk = risk

    def get_name(self):
        return self.__name

    def take(self, card):
        self.__hand.append(card)

    # returns total value of cards in hand
    def total(self):
        totals = [0, 0]
        total = 0
        aces_in_hand = self.get_aces()

        for card in self.__hand:
            card_val = card.get_int_value()

            # Add value of card to total, deal with aces if we have them next
            if card_val != 1:
                total += card_val

        if aces_in_hand == 0:
            totals[0] = total
            totals[1] = -1
        else:
            totals[0] = total + 11 + aces_in_hand - 1
            totals[1] = total + aces_in_hand
            
        return totals

    def get_aces(self):
        num_aces = 0
        for card in self.__hand:
            if card.get_int_value == 1:
                num_aces += 1
        return num_aces

    def toString(self):
        txt = self.__name + ": "
        for card in self.__hand:
            txt += "[" + card.toString() + "] "
        return txt
