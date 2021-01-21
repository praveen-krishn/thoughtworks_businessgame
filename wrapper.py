from app import App
import csv

input_file = "/Users/praveenkrishnan/Documents/src/myproject/ThoughtWorks/BusinessGame/BusinessGame/data.csv"
with open(input_file, 'r') as f:
    csv_reader = csv.DictReader(f, delimiter=',', quotechar='"')
    for row in csv_reader:
        d = dict(row)
        cells = d["cells"]
        dice = d["dice"]
        players = d["players"]
        players = int(players)
        cells_lst = cells.strip().split(",")
        dice_lst = dice.strip().split(",")
        print("")
        print("Cells:", cells)
        print("Dice:", dice)
        print("players:", players)
        print("Result:")
        a = App(cells_lst, dice_lst, players)
        a.play(False, False)
        a.summary()
