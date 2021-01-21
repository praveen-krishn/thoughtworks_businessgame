class Player():
    def __init__(self, name, cash):
        self.name = name
        self.__cash = cash
        self.__worth = 0
        self.__position = 0

    @property
    def cash(self):
        return self.__cash

    @cash.setter
    def cash(self, amount):
        self.__cash = amount

    @property
    def worth(self):
        return self.__worth

    @worth.setter
    def worth(self, worth):
        self.__worth = worth

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position

    def __str__(self):
        return "{} has total money {:>5} and asset of amount: {:>5}".format(self.name, self.cash, self.worth)


# class PlayerPlay():
#     def __call__(self, Player, Board, roll):
#         pass
