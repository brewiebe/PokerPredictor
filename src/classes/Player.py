class Player:

    def __init__(self, name, risk, dealer=False):
        self.__name = name
        # cards player is holding
        self.__hand = []
        # probability of getting blackjack needed for player to draw
        self.__risk = risk
        self.__stayed = False
        self.__dealer = dealer

    def get_name(self):
        return self.__name

    def take(self, card):
        self.__hand.append(card)

    def get_dealer(self):
        return self.__dealer

    def get_stayed(self):
        return self.__stayed

    def set_stayed(self, stayed):
        self.__stayed = stayed

    # returns total value of cards in hand
    def total(self):
        totals = []
        total = 0
        aces_in_hand = self.get_aces()

        for card in self.__hand:
            card_val = card.get_int_value()

            # Add value of card to total, deal with aces if we have them next
            if card_val != 1:
                total += card_val

        if aces_in_hand == 0:
            totals.append(total)
        else:
            totals.append(total + 11 + aces_in_hand - 1)
            totals.append(total + aces_in_hand)
            
        return totals

    def highest_total(self):
        totals = self.total()
        highest = 0

        for total in totals:
            if total > highest:
                highest = total

        return highest

    def highest_under(self, under):
        totals = self.total()
        highest = 0

        for total in totals:
            if  highest < total <= under:
                highest = total

        return highest

    def get_aces(self):
        num_aces = 0
        for card in self.__hand:
            if card.get_int_value() == 1:
                num_aces += 1
        return num_aces

    def hit(self, prob_win):
        if prob_win > self.__risk or (prob_win == 0 and self.highest_total() < 21):
            return True
        elif self.__dealer and self.highest_total() < 17:
            return True
        else:
            return False

    def busted(self):
        for total in self.total():
            if total <= 21:
                return False
        return True


    def to_string(self):
        txt = self.__name + ": "
        for card in self.__hand:
            txt += "[" + card.toString() + "] "
        return txt
