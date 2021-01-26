# Business Game

By: Praveen Krishnan

[LinkedIn](https://www.linkedin.com/in/praveenkm/)

## Assumptions

Starting Point or first dice roll will gain entry to the board.
There is no cell as "Starting Point" in the board, its outside the board.

In sample output for both use cases given: "Balance at Bank" is wrong.

## Design Principles
- Composition over Inheritence
- Duck Typing Objects
- Instances like functions using __ __call__ __ method

## Environment
```sh
bash-3.2$ python -V
Python 3.7.6
```
## Notes

shebang not added in any python files intentionally, to ensure to work on deployed instance

## Setting up project
1. unzip BusinessGame.zip
2. cd BusinessGame

## Output
DataSet:
```sh
bash-3.2$ cat data.csv 
cells,dice,players
"J,H,L,H,E,L,H,L,H,J","2,2,1,4,4,2,4,4,2,2,2,1,4,4,2,4,4,2,2,2,1",3
"J,H,L,H,E,L,H,L,H,J","2,2,1,4,2,3,4,1,3,2,2, 7,4,7,2,4,4,2,2,2,2",3
```

## Executing wrapper using dataset:
```sh
bash-3.2$ python wrapper.py 
Cells: J,H,L,H,E,L,H,L,H,J
Dice: 2,2,1,4,4,2,4,4,2,2,2,1,4,4,2,4,4,2,2,2,1
players: 3
Result:
Player-1 has total money  1100 and asset of amount:   500
Player-2 has total money   600 and asset of amount:     0
Player-3 has total money  1150 and asset of amount:     0
Balance at Bank: 2150

Cells: J,H,L,H,E,L,H,L,H,J
Dice: 2,2,1,4,2,3,4,1,3,2,2, 7,4,7,2,4,4,2,2,2,2
players: 3
Result:
Player-1 has total money   650 and asset of amount:   500
Player-2 has total money   750 and asset of amount:   300
Player-3 has total money   850 and asset of amount:   200
Balance at Bank: 2750
```

## Executing UnitTests
```sh
bash-3.2$ python -m unittest -v test
test_BankCash (test.TestBanker) ... ok
test_BankCredit (test.TestBankerCredit) ... ok
test_BankDebit (test.TestBankerDebit) ... ok
test_BankWithoutCash (test.TestBankerDebit) ... ok
test_Board (test.TestBoard) ... ok
test_BoardBuildCells (test.TestBoard) ... ok
test_BoardGetData (test.TestBoard) ... ok
test_BoardGetSize (test.TestBoard) ... ok
test_BoardSetData (test.TestBoard) ... ok
test_PlayerCash (test.TestPlayer) ... ok
test_PlayerDetails (test.TestPlayer) ... ok
test_PlayerWorth (test.TestPlayer) ... ok
test_PlayerBuysHotel (test.TestPlayerInHotel) ... ok
test_PlayerUpgradeHotelGold (test.TestPlayerInHotel) ... ok
test_PlayerUpgradeHotelPlatinum (test.TestPlayerInHotel) ... ok
test_PlayerInJail (test.TestPlayerInJail) ... ok
test_PlayerInJailWithoutCash (test.TestPlayerInJail) ... ok
test_BankWithoutCash (test.TestPlayerInLottery) ... ok
test_PlayerInLottery (test.TestPlayerInLottery) ... ok

----------------------------------------------------------------------
Ran 19 tests in 0.002s

OK
bash-3.2$
```
## TestCoverage
```sh
bash-3.2$ coverage run test.py
...................
----------------------------------------------------------------------
Ran 19 tests in 0.002s

OK
bash-3.2$ coverage report
Name              Stmts   Miss  Cover
-------------------------------------
app.py               64     52    19%
lib/Banker.py        22      1    95%
lib/Board.py         24      1    96%
lib/Events.py        61      1    98%
lib/Player.py        20      3    85%
lib/__init__.py       4      0   100%
test.py             147      0   100%
-------------------------------------
TOTAL               342     58    83%
bash-3.2$
```
