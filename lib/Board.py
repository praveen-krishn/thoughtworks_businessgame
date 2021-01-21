import json


class Board():
    _singleton = None
    ds = dict()

    def __new__(cls):
        if not cls._singleton:
            cls._singleton = super(Board, cls).__new__(cls)
        return cls._singleton

    def __init__(self):
        pass

    def buildCells(self, list_of_cells: list):
        for l in range(len(list_of_cells)):
            rec = dict()
            rec["classify"] = list_of_cells[l]
            rec["ownedby"] = "Bank"
            # if list_of_cells[l] == "H":
            #     rec["hotel_type"] = "silver"
            self.ds[str(l)] = rec

    def getSize(self):
        return len(self.ds.keys())

    def getdata(self, pos):
        return self.ds[str(pos)]

    def set(self, pos, val):
        self.ds[str(pos)] = val

    def __str__(self):
        return json.dumps(self.ds)
