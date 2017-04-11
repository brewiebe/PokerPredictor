class Game:

    def __init__(self, players, deck):
        self.__players = players
        self.__deck = deck
        self.__exposed = []

    def start_game(self):
        # Deal two cards to each player
        for x in range(2):
            for player in self.__players:
                card = self.__deck.draw()

                # Add each dealt card to the known cards, except for the first dealer card as it is face down ass up
                if player.get_name() != "Dealer" or x != 0:
                    self.__exposed.append(card)

                player.take(card)

    def get_exposed(self):
        return self.__exposed

    def get_players(self):
        return self.__players

    def get_dealer(self):
        for player in self.__players:
            if player.get_dealer():
                return player

    def get_highest(self):
        highest = 0

        for player in self.__players:
            player_total = player.total()
            for total in player_total:
                if total > highest and total <= 21:
                    highest = total

        return highest

    def get_highest_player(self):
        highest = 0
        highest_player = None

        for player in self.__players:
            player_total = player.total()
            for total in player_total:
                if total > highest and total <= 21:
                    highest = total
                    highest_player = player

        return highest_player

    def all_players_stayed(self):
        for player in self.__players:
            if not player.get_stayed() and not player.get_dealer():
                return False
        return True

    def play_game(self, predictor):
        while not self.all_players_stayed():
            for player in self.__players:
                if not player.get_dealer() and not player.get_stayed():
                    prob_win = predictor.probability_win(player, 19)

                    if player.hit(prob_win):
                        card = self.__deck.draw()
                        self.__exposed.append(card)
                        player.take(card)
                    else:
                        player.set_stayed(True)

        dealer = self.get_dealer()

        while not dealer.get_stayed():
            prob_win = predictor.probability_win(dealer, 19)

            if dealer.hit(prob_win):
                card = self.__deck.draw()
                self.__exposed.append(card)
                dealer.take(card)
            else:
                dealer.set_stayed(True)

    def get_winner(self):
        winners = []
        dealer = self.get_dealer()

        # If dealer busts all non busted players win
        if dealer.busted():
            for player in self.__players:
                if not player.busted():
                    winners.append(player)
        else:
            for player in self.__players:
                if not player.busted():
                    for total in player.total():
                        if dealer.highest_under(21) < total <= 21:
                            winners.append(player)

        if len(winners) == 0:
            winners.append(dealer)

        return winners

