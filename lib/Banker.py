class Banker():
    _singleton = None

    def __new__(cls):
        if not cls._singleton:
            cls._singleton = super(Banker, cls).__new__(cls)
        return cls._singleton

    def __init__(self):
        self.__cash = 0

    @property
    def cash(self):
        return self.__cash

    @cash.setter
    def cash(self, amount):
        self.__cash = amount

    def __str__(self):
        return "Balance at Bank: {}".format(self.cash)


class BankerDebit():
    # class can be singleton

    def __call__(self, BankerObj, amount):
        # instance is called as a function
        # print("debit from BankerCredit Class")
        if BankerObj.cash-amount < 0:
            raise Exception(
                "{}: Cash Balance Negative, cannot debit from bank".format(
                    self.__class__))
        BankerObj.cash -= amount


class BankerCredit():
    # class can be singleton

    def __call__(self, BankerObj, amount):
        # instance is called as a function
        # print("Credit from BankerCredit Class")
        BankerObj.cash += amount
