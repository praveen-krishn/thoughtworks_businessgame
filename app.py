from lib.Banker import Banker, BankerDebit, BankerCredit
from lib.Player import Player
from lib.Board import Board
from lib.Events import PlayerInJail, PlayerInLottery, PlayerInHotel


class App():
    MAX_ROUNDS = 10
    Initial_Money_Bank = 5000
    Initial_Money_Player = 1000

    players = dict()

    def __init__(self, list_of_cells: list, dice: list, player_count: int):
        if not isinstance(player_count, int):
            raise TypeError(
                "{}, Player Count should be integer".format(self.__class__))

        if player_count < 2:
            raise ValueError(
                "{}, Player Count should be greater than 2".format(self.__class__))

        if len(dice) > (self.MAX_ROUNDS*player_count):
            raise ValueError(
                "{}, Game cannot be more than 10 rounds".format(self.__class__))

        self.list_of_cells = list_of_cells
        self.dice = dice
        self.player_count = player_count

        self.bank = Banker()
        self.bank.cash = self.Initial_Money_Bank
        bank_debit = BankerDebit()

        self.board = Board()
        self.board.buildCells(list_of_cells)

        for p in range(player_count):
            player_name = "Player-"+str(p+1)
            bank_debit(self.bank, self.Initial_Money_Player)
            self.players[player_name] = Player(
                player_name, self.Initial_Money_Player)

    def play(self, debug_turns: bool = False, debug_rounds: bool = False):
        count = 0
        rounds = 0
        number_of_players = len(self.players.keys())
        for d in self.dice:
            player_key = "Player-"+str(count % number_of_players + 1)

            player_pos = self.players[player_key].position + int(d)
            if rounds == 0:
                player_pos -= 1
            player_pos = player_pos % len(self.list_of_cells)
            # player_pos = player_pos % (len(self.list_of_cells)+1)
            self.players[player_key].position = player_pos
            # print(player_pos)
            cell = self.board.getdata(player_pos)

            if cell["classify"] == "J":
                player_in_jail = PlayerInJail()
                player_in_jail(self.players[player_key], self.bank)

            if cell["classify"] == "L":
                player_in_lottery = PlayerInLottery()
                player_in_lottery(self.players[player_key], self.bank)

            if cell["classify"] == "H":
                player_in_hotel = PlayerInHotel()
                player_in_hotel(self.players, player_key,
                                self.bank, cell, player_pos)

            if debug_turns:
                print(player_key, "dice", d, "position:", player_pos,
                      self.players[player_key].cash, self.bank.cash, cell)

            count += 1

            if count % len(self.players.keys()) == 0:
                rounds += 1
                if debug_rounds:
                    print("Round:", end=" ", flush=True)
                    print(rounds, end=" ", flush=True)
                    for k in self.players.keys():
                        print('{:>8}'.format(
                            self.players[k].cash), end=" ", flush=True)
                    print('{:>8}'.format(self.bank.cash))

    def summary(self):
        for k in self.players.keys():
            print(self.players[k])
        print(self.bank)
        # print(self.board)
