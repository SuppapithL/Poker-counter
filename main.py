import sys, subprocess
import random

class playerinit:
    def __init__(self, name,  number, point):
        self.num = number
        self.point = point
        self.name = name

    def playerinfo(self):
        return f"Num: {self.num},Name: {self.name},Point: {self.point}"

    def updateinfo(self, newpoint):
        self.point = newpoint

class Table:
    def __init__(self, players):
        self.players = players
        self.pot = 0
        self.turn_index = 0
        self.dealer = random.choice(players)
    
    def tableinfo(self):
        package = []
        for player in self.players:
            package.append(f"Num: {player.num},Name: {player.name},Point: {player.point},Dealer: {player == self.dealer}")
        return package

def get_int(prompt, min_val=None, max_val=None):
    while True:
        raw = input(prompt)

        try:
            value = int(raw)
            
        except ValueError:
            print("Invalid integer.")
            continue

        if min_val is not None and value < min_val:
            print("Too small.")
            continue

        if max_val is not None and value > max_val:
            print("Too large.")
            continue

        return value

def clearconsole():
    os = sys.platform
    if os in ('linux', 'darwin'):
        command = 'clear'
    elif os == 'win32':
        command = 'cls'
    subprocess.run(command, shell = True)

def Lobby(Players):
    clearconsole()
    print ("This is Lobby!\nPlayers information:")
    for identity in Players:
        print(identity.playerinfo())
    staged = input("Please enter number of the player that will join(x,y,...):").split(",")
    Joined = []
    for Nums in staged:
        if int(Nums) < len(staged) + 1:
            Joined.append(Players[int(Nums)])
    clearconsole()
    Tables(Joined)

def Setup():
    rawplayers = []
    players = []
    while True:
        clearconsole()
        print(f'This is Player setup!\nCurrent players:')
        for identity in players:
            print(identity.playerinfo())
        print()
        command = input("a: add player\nr: remove player\nu: update player's information\nc: continue\nq: quit\nPlease enter your command:".lower())
        match command:
            case "a":
                players = addplayer(players)
            case "r":
                players = removeplayer(players)
            case "u":
                pass
            case "c":
                break
            case "q":
                exit()
            case _:
                input("Invalid command please try again") 
    return players

def addplayer(players):
    clearconsole() 
    print("This is add player!") 
    Name = input("Please enter player name:")
    Point = int(input("Please enter player starting point:"))
    allindex = []
    for number in players:
        allindex.append(number.num)
    index = max([0]+allindex) + 1
    Player = playerinit(Name, index, Point)
    players.append(Player)
    return players

def removeplayer(players):
    return

def Tables(Joined):
    clearconsole()
    Tabl = Table(Joined)
    print("This is Table, Joined player:")
    for element in Tabl.tableinfo():
        print(element)

def main():
    Players = Setup()
    Lobby(Players)

main()
