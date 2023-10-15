from Player import *
print("__________ Welcome to BANK HACK! __________")
player = Player(input("Please enter your name: "), input("Please enter your email: "))
if not player.verify():
    SystemExit

