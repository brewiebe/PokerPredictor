class Player:

    def __init__(self, name, risk):
        self.__name = name
        #cards player is holding
        self.__hand = []
        #probablility of getting blackjack needed for player to draw
        self.__risk = risk

    def get_name(self):
        return self.__name

    def take(self, card):
        self.__hand.append(card)

    #returns total value of cards in hand
    def total(self):
        total = 0
        aces_in_hand = 0
        for card in self.__hand:
            card_val = card.get_int_value()

            # it's an ace, need to decide whether to count it as 1 or 11 at the end
            if card_val == 1:
                aces_in_hand += 1
            else:
                total += card_val

        for x in range(aces_in_hand):
            #taking ace as 11 will bust
            if total + 11 > 21:
                total += 1
            #taking ace as 11 wont bust
            elif total + 11 <= 21:
                #if only one ace take as 11
                if aces_in_hand == 1:
                    total += 11
                #if more than one ace but the rest of the aces won't cause hand to bust
                elif aces_in_hand > 1 and (total + 11 + aces_in_hand) <= 21:
                    total += 11
                #if the rest of the aces cause the hand to bust
                else:
                    total += 1
        return total

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
