import unittest

from app import App
from lib.Banker import BankerDebit, BankerCredit, Banker
from lib.Player import Player
from lib.Board import Board
from lib.Events import *


class TestBanker(unittest.TestCase):
    def test_BankCash(self):
        a = Banker()
        b = Banker()
        self.assertEqual(a, b)
        a.cash = 300
        self.assertEqual(a.cash, 300)
        self.assertEqual(b.cash, 300)
        b.cash -= 100
        self.assertEqual(a.cash, 200)
        b.cash -= a.cash
        self.assertEqual(a.cash, 0)


class TestBankerCredit(unittest.TestCase):
    def test_BankCredit(self):
        bank = Banker()
        bankcredit = BankerCredit()
        bankcredit(bank, 200)
        self.assertEqual(bank.cash, 200)


class TestBankerDebit(unittest.TestCase):
    def setUp(self):
        self.bank = Banker()
        self.bankcredit = BankerCredit()
        self.bankdebit = BankerDebit()

    def test_BankDebit(self):
        self.bankcredit(self.bank, 200)
        self.assertEqual(self.bank.cash, 200)
        self.bankdebit(self.bank, 100)
        self.assertEqual(self.bank.cash, 100)

    def test_BankWithoutCash(self):
        with self.assertRaises(Exception):
            self.bankdebit(self.bank, 10000)


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("alpha", 500)

    def test_PlayerDetails(self):
        self.assertTrue(self.player.name)
        self.assertEqual(self.player.name, "alpha")

    def test_PlayerCash(self):
        self.assertEqual(self.player.cash, 500)
        self.assertNotEqual(self.player.cash, 100)

    def test_PlayerWorth(self):
        self.assertEqual(self.player.worth, 0)
        self.player.worth = 100
        self.assertEqual(self.player.worth, 100)


class TestBoard(unittest.TestCase):
    def test_Board(self):
        a = Board()
        b = Board()
        self.assertEqual(a, b)

    def setUp(self):
        self.board = Board()
        self.sample = {'0': {'classify': 'H', 'ownedby': 'Bank'},
                       '1': {'classify': 'J', 'ownedby': 'Bank'}}

    def test_BoardBuildCells(self):
        self.board.buildCells(["H", "J"])
        self.assertEqual(self.board.ds, self.sample)

    def test_BoardGetSize(self):
        self.assertEqual(self.board.getSize(), 2)

    def test_BoardGetData(self):
        self.assertEqual(self.board.getdata(1),
                         {'classify': 'J', 'ownedby': 'Bank'})

    def test_BoardSetData(self):
        actual_data = self.board.getdata(1)
        err_data = "{'classify': 'unknown', 'ownedby': 'Bank'}"
        self.board.set(1, err_data)
        self.assertEqual(self.board.getdata(1), err_data)
        self.assertNotEqual(self.board.getdata(1), actual_data)


class TestPlayerInJail(unittest.TestCase):
    def setUp(self):
        self.bank = Banker()
        self.player1 = Player("Player-1", 1000)
        self.player_in_jail = PlayerInJail()

    def test_PlayerInJail(self):
        self.assertEqual(self.bank.cash, 0)
        self.assertEqual(self.player1.cash, 1000)
        self.player_in_jail(self.player1, self.bank)
        self.assertEqual(self.bank.cash, 150)
        self.assertEqual(self.player1.cash, 1000-150)

    def test_PlayerInJailWithoutCash(self):
        self.player1.cash = 100
        with self.assertRaises(Exception):
            self.player_in_jail(self.player1, self.bank)


class TestPlayerInLottery(unittest.TestCase):
    def setUp(self):
        self.bank = Banker()
        self.bank.cash = 1000

        self.player1 = Player("Player-1", 1000)
        self.player_in_lottery = PlayerInLottery()

    def test_PlayerInLottery(self):
        self.player_in_lottery(self.player1, self.bank)
        self.assertEqual(self.bank.cash, 1000-200)
        self.assertEqual(self.player1.cash, 1000+200)

    def test_BankWithoutCash(self):
        self.bank.cash = 100
        with self.assertRaises(Exception):
            self.player_in_lottery(self.player1, self.bank)


class TestPlayerInHotel(unittest.TestCase):
    def setUp(self):

        # self.board = Board()
        # self.board.buildCells(["H", "E"])
        # # self.cell = self.board.ds["0"]
        self.cell = {'classify': 'H', 'ownedby': 'Bank'}
        self.player1 = Player("Player-1", 1000)
        self.player2 = Player("Player-2", 1000)

        self.all_players = dict()
        self.all_players["Player-1"] = self.player1
        self.all_players["Player-2"] = self.player2

        self.bank = Banker()
        self.player_in_hotel = PlayerInHotel()

    def test_PlayerBuysHotel(self):
        self.player_in_hotel(self.all_players, "Player-1",
                             self.bank, self.cell, 0)
        # print(self.cell)
        self.assertEqual(self.cell["ownedby"], "Player-1")
        self.assertEqual(self.cell["hotel_type"], "silver")
        self.assertEqual(self.player1.cash, 800)

        self.player_in_hotel(self.all_players, "Player-2",
                             self.bank, self.cell, 0)
        self.assertEqual(self.player1.cash, 850)
        self.assertEqual(self.player2.cash, 950)

    def test_PlayerUpgradeHotelGold(self):
        self.player1.cash = 500
        self.player_in_hotel(self.all_players, "Player-1",
                             self.bank, self.cell, 0)
        self.assertEqual(self.cell["ownedby"], "Player-1")
        self.assertEqual(self.cell["hotel_type"], "silver")
        self.assertEqual(self.player1.cash, 300)
        # print(self.cell, self.player1.cash, self.player2.cash)

        self.player_in_hotel(self.all_players, "Player-1",
                             self.bank, self.cell, 0)
        self.assertEqual(self.cell["hotel_type"], "gold")
        self.assertEqual(self.player1.cash, 200)
        # print(self.cell, self.player1.cash, self.player2.cash)

        self.player_in_hotel(self.all_players, "Player-2",
                             self.bank, self.cell, 0)
        self.assertEqual(self.player1.cash, 350)
        self.assertEqual(self.player2.cash, 850)

    def test_PlayerUpgradeHotelPlatinum(self):
        self.player1.cash = 1000
        self.player_in_hotel(self.all_players, "Player-1",
                             self.bank, self.cell, 0)
        self.assertEqual(self.cell["ownedby"], "Player-1")
        self.assertEqual(self.cell["hotel_type"], "silver")
        self.assertEqual(self.player1.cash, 800)

        self.player_in_hotel(self.all_players, "Player-1",
                             self.bank, self.cell, 0)
        self.assertEqual(self.cell["hotel_type"], "gold")
        self.assertEqual(self.player1.cash, 700)

        self.player_in_hotel(self.all_players, "Player-1",
                             self.bank, self.cell, 0)
        self.assertEqual(self.cell["hotel_type"], "platinum")
        self.assertEqual(self.player1.cash, 500)

        self.player_in_hotel(self.all_players, "Player-2",
                             self.bank, self.cell, 0)
        self.assertEqual(self.player1.cash, 500+300)
        self.assertEqual(self.player2.cash, 1000-300)


if __name__ == '__main__':
    unittest.main()
