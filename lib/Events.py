from .Banker import BankerCredit, BankerDebit
from .Board import Board


class PlayerInJail():
    def __call__(self, PlayerObj, BankObj):
        # print("Player pays Bank")
        penalty = 150
        if PlayerObj.cash >= penalty:
            PlayerObj.cash -= penalty
            bank_credit = BankerCredit()
            bank_credit(BankObj, penalty)
        else:
            raise Exception(
                "Player: {} do not have enough money to pay bank".format(PlayerObj.name))


class PlayerInLottery():
    def __call__(self, PlayerObj, BankObj):
        # print("Bank pays Player")
        award = 200
        if BankObj.cash >= award:
            PlayerObj.cash += award
            bank_debit = BankerDebit()
            bank_debit(BankObj, award)
        else:
            raise Exception(
                "Bank do not have enough money to pay Player: {}".format(PlayerObj.name))


class PlayerInHotel():
    def __call__(self, all_players: dict, current_player_name: str, BankObj, cell: dict, position):
        hotel_category = {}
        hotel_category["silver"] = {"value": 200, "rent": 50}
        hotel_category["gold"] = {"value": 300, "rent": 150}
        hotel_category["platinum"] = {"value": 500, "rent": 300}

        # print(hotel_category, cell)
        PlayerObj = all_players[current_player_name]
        bank_credit = BankerCredit()

        if cell["ownedby"] == "Bank":
            if PlayerObj.cash >= hotel_category["silver"]["value"]:
                # print("Player will buy hotel")
                cell["ownedby"] = PlayerObj.name
                cell["hotel_type"] = "silver"
                board = Board()
                board.set(position, cell)
                PlayerObj.cash -= hotel_category["silver"]["value"]
                PlayerObj.worth += hotel_category["silver"]["value"]
                bank_credit(BankObj, hotel_category["silver"]["value"])

        elif cell["ownedby"] == PlayerObj.name:
            # print("Player will upgrade hotel")

            if cell["hotel_type"] == "silver":
                excess = hotel_category["gold"]["value"] - \
                    hotel_category["silver"]["value"]

                if PlayerObj.cash >= excess:
                    # print("Player will upgrade hotel to gold")
                    cell["hotel_type"] = "gold"
                    board = Board()
                    board.set(position, cell)
                    PlayerObj.cash -= excess
                    PlayerObj.worth += excess
                    bank_credit(BankObj, excess)

            elif cell["hotel_type"] == "gold":
                excess = hotel_category["platinum"]["value"] - \
                    hotel_category["gold"]["value"]

                if PlayerObj.cash >= excess:
                    # print("Player will upgrade hotel to platinum")
                    cell["hotel_type"] = "platinum"
                    board = Board()
                    board.set(position, cell)
                    PlayerObj.cash -= excess
                    PlayerObj.worth += excess
                    bank_credit(BankObj, excess)
            else:
                pass

        else:
            if PlayerObj.name != cell["ownedby"]:
                # print("{} pays rent".format(PlayerObj.name))
                OwnerPlayer = all_players[cell["ownedby"]]
                if PlayerObj.cash >= hotel_category[cell["hotel_type"]]["rent"]:
                    PlayerObj.cash -= hotel_category[cell["hotel_type"]]["rent"]
                    OwnerPlayer.cash += hotel_category[cell["hotel_type"]]["rent"]
                else:
                    raise Exception("Player: {} do not have enough money to pay Hotel Owner {}".format(
                        PlayerObj.name, OwnerPlayer.name))
