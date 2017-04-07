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
